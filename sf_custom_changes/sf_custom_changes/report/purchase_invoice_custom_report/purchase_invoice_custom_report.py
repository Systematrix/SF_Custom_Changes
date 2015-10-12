# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, msgprint

def execute(filters=None):
	if not filters: filters = {}
	
	columns = get_columns()
	data = get_entries(filters)
	
	return columns, data
	
def get_columns():
	return [_("ID") + ":Link/Sales Invoice:140", _("Supplier Name") + ":Link/Supplier:140", _("Supplier Invoice No") +  ":Data:130",
                _("Supplier Invoice Date") +  ":Date:140", _("Grand Total") +  ":Currency:100", _("Due Date") +  ":Date:100", 
                _("Outstanding Amount") +  ":Currency:120",
                _("Credit Days") +  ":Data:100"
	]

def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"): conditions += " posting_date>=%(from_date)s"
	if filters.get("to_date"): conditions += " and posting_date<=%(to_date)s"
	if filters.get("supplier"): conditions += " and supplier=%(supplier)s"
	
	return conditions
	
def get_entries(filters):
	conditions = get_conditions(filters)
	entries =  frappe.db.sql("""select name, supplier_name, bill_no, bill_date, grand_total_import, due_date, outstanding_amount, credit_days from `tabPurchase Invoice` where  %s order by name DESC""" % conditions, filters, as_list=1)
	return entries
