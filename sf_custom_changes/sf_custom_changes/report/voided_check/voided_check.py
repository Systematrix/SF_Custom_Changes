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
	return [_("Posting Date") + ":Date:100",_("Journal Voucher") + ":Link/Journal Voucher:140", _("Account") + ":Link/Account:140", 
		 _("Debit") + ":Currency:120", _("Credit") + ":Currency:120",
                 _("Against Account") + ":Link/Account:200", 
		_("Check#") + ":Data:120",_("Check Date") + ":Date:110",_("Clearance Date") + ":Date:110"
	]

def get_conditions(filters):
	conditions = ""
	if not filters.get("account"):
		msgprint(_("Please select Bank Account"), raise_exception=1)
	else:
		conditions += " and jvd.account = %(account)s"

	if filters.get("include_cancelled_jv"):
                conditions += "and jv.docstatus=2"
        else:
                conditions += "and jv.docstatus=1"
		
	if filters.get("from_date"): conditions += " and jv.posting_date>=%(from_date)s"
	if filters.get("to_date"): conditions += " and jv.posting_date<=%(to_date)s"
	
	return conditions
	
def get_entries(filters):
	conditions = get_conditions(filters)
	entries =  frappe.db.sql("""select jv.posting_date, jv.name, jvd.account, 
		jvd.debit, jvd.credit, jvd.against_account, jv.cheque_no, jv.cheque_date,jv.clearance_date
		from `tabJournal Voucher Detail` jvd, `tabJournal Voucher` jv 
		where jvd.parent = jv.name  %s and jv.cheque_no is not null and jv.cheque_no REGEXP '^[0-9]+$' and jvd.debit is null
		order by jv.name DESC""" % conditions, filters, as_list=1)
	return entries
