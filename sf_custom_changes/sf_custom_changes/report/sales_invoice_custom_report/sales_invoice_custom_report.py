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
	return [_("ID") + ":Link/Sales Invoice:140", _("Date") +  ":Date:140", _("Customer Name") + ":Link/Customer:140", _("Customer PO NO.") +  ":Data:100",
                _("Grand Total") +  ":Currency:100", _("Due Date") +  ":Date:100", _("Outstanding Amount") +  ":Currency:140",
                _("Credit Days") +  ":Data:100"
	]

def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"): conditions += " posting_date>=%(from_date)s"
	if filters.get("to_date"): conditions += " and posting_date<=%(to_date)s"
	if filters.get("customer"): conditions += " and customer=%(customer)s"
	
	return conditions
	
def get_entries(filters):
	conditions = get_conditions(filters)
	entries =  frappe.db.sql("""select name, posting_date, customer_name, po_no, grand_total_export, due_date, outstanding_amount, credit_days from `tabSales Invoice` where  %s and docstatus!=2 order by name DESC""" % conditions, filters, as_list=1)
	return entries
