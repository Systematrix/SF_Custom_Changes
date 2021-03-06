# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns(filters)
	item_map = get_item_details(filters)
	iwb_map = get_item_warehouse_batch_map(filters)
        total_bal_qty = 0
        total_val_rate =0
        total_batch_value = 0
	data = []
	for item in sorted(iwb_map):
		for wh in sorted(iwb_map[item]):
			for batch in sorted(iwb_map[item][wh]):
				qty_dict = iwb_map[item][wh][batch]
				data.append([item, item_map[item]["item_name"],
					item_map[item]["net_weight"],item_map[item]["weight_uom"],item_map[item]["stock_uom"],
                                        wh, batch, qty_dict.warehouse_lot,
					qty_dict.bal_qty, qty_dict.stock_val, (flt(qty_dict.stock_val)*flt(qty_dict.bal_qty)),
                                        qty_dict.opening_qty,  qty_dict.in_qty, 
					qty_dict.out_qty, 
				])
                                total_bal_qty +=qty_dict.bal_qty
                                total_batch_value +=(flt(qty_dict.stock_val)*flt(qty_dict.bal_qty))
                                

	#add total row
	data.append(['Total','','','','','','','',total_bal_qty,'',total_batch_value,'','',''])

	return columns, data

def get_columns(filters):
	"""return columns based on filters"""

	columns = [_("Item") + ":Link/Item:100"] + [_("Item Name") + "::150"] + \
	 [_("Net Weight") + ":Float:80"] +  [_("Fill") + ":Link/UOM:90"] + [_("Stock UOM") + ":Link/UOM:90"] + \
         [_("Warehouse") + ":Link/Warehouse:100"] + [_("Batch") + ":Link/Batch:150"] +[_("Warehouse Lot") + ":Data:150"] + \
         [_("Balance Qty") + ":Float:90"] + [_("Valuation Rate") + ":Currency:100"] + [_("Batch Value") + ":Currency:100"] + \
         [_("Opening Qty") + ":Float:90"] + [_("In Qty") + ":Float:80"] + [_("Out Qty") + ":Float:80"]
         

	return columns

def get_conditions(filters):
	conditions = ""
	if not filters.get("from_date"):
		frappe.throw(_("'From Date' is required"))

	if filters.get("to_date"):
		conditions += " and posting_date <= '%s'" % filters["to_date"]
	else:
		frappe.throw(_("'To Date' is required"))

	return conditions

#get all details
def get_stock_ledger_entries(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select item_code, batch_no, warehouse,
		posting_date, actual_qty,
                 CASE
                WHEN batch_no !='' then
                (select warehouse_lot_id from `tabBatch` where name=batch_no)
                ELSE " "
                END AS warehouse_lot,
		CASE
                WHEN batch_no !='' then
                ( select sum(stock_value_difference)/sum(actual_qty) from `tabStock Ledger Entry` b where b.batch_no = c.batch_no  group by 			batch_no)
                ELSE " "
                END AS stock_val
		from `tabStock Ledger Entry` c
		where docstatus < 2 %s order by item_code, warehouse""" %
		conditions, as_dict=1)

def get_item_warehouse_batch_map(filters):
	float_precision = cint(frappe.db.get_default("float_precision")) or 3
	sle = get_stock_ledger_entries(filters)
	iwb_map = {}

	for d in sle:
		iwb_map.setdefault(d.item_code, {}).setdefault(d.warehouse, {})\
			.setdefault(d.batch_no, frappe._dict({
				"opening_qty": 0.0, "in_qty": 0.0, "out_qty": 0.0, "bal_qty": 0.0, "batch_value": 0.0
			}))
		qty_dict = iwb_map[d.item_code][d.warehouse][d.batch_no]
                qty_dict.warehouse_lot = d.warehouse_lot
		if d.posting_date < filters["from_date"]:
			qty_dict.opening_qty += flt(d.actual_qty, float_precision)
		elif d.posting_date >= filters["from_date"] and d.posting_date <= filters["to_date"]:
                        qty_dict.stock_val = d.stock_val
			if flt(d.actual_qty) > 0:
				qty_dict.in_qty += flt(d.actual_qty, float_precision)
			else:
				qty_dict.out_qty += abs(flt(d.actual_qty, float_precision))

		qty_dict.bal_qty += flt(d.actual_qty, float_precision)

	return iwb_map

def get_item_details(filters):
	item_map = {}
	for d in frappe.db.sql("select name, item_name, net_weight, stock_uom, weight_uom from tabItem", as_dict=1):
		item_map.setdefault(d.name, d)

	return item_map
