# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils import flt
from erpnext.accounts.report.accounts_receivable.accounts_receivable import get_ageing_data

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns(filters)
	entries = get_entries(filters)
	invoice_posting_date_map = get_invoice_posting_date_map(filters)
	against_date = ""
	outstanding_amount = 0.0

	data = []
	for d in entries:
		if d.against_voucher:
			against_date = d.against_voucher and invoice_posting_date_map[d.against_voucher] or ""
			outstanding_amount = flt(d.debit) or -1*flt(d.credit)
		else:
			against_date = d.against_invoice and invoice_posting_date_map[d.against_invoice] or ""
			outstanding_amount = flt(d.credit) or -1*flt(d.debit)

		row = [d.posting_date, d.name, d.cheque_no, d.cheque_date, d.account, d.against_voucher or d.against_invoice,
			against_date, d.debit, d.credit,  d.remark]

		if d.against_voucher or d.against_invoice:
			row += get_ageing_data(d.posting_date, against_date, outstanding_amount)
		else:
			row += ["", "", "", "", ""]

		data.append(row)

	return columns, data

def get_columns(filters):
    linkType = ""
    if filters.get("payment_type") == "Incoming":
        linkType = "Sales Invoice"
    else:
        linkType = "Purchase Invoice"

    return [ _("Posting Date") + ":Date:100",_("Journal Voucher") + ":Link/Journal Voucher:140",
        _("Reference No") + "::100", _("Reference Date") + ":Date:100", _("Account") + ":Link/Account:140",
         _("Against Invoice") + ":Link/"+linkType+":130",
        _("Against Invoice Posting Date") + ":Date:130", _("Debit") + ":Currency:120", _("Credit") + ":Currency:120",
        _("Remarks") + "::150", _("Days to Pay") + ":Int:100",
        "0-30:Currency:100", "30-60:Currency:100", "60-90:Currency:80", _("90-Above") + ":Currency:100"
        ]
        
def get_conditions(filters):
	conditions = ""
	party_accounts = []

	if filters.get("account"):
		party_accounts = [filters["account"]]
	else:
		cond = filters.get("company") and (" and company = '%s'" %
			filters["company"].replace("'", "\'")) or ""

		if filters.get("payment_type") == "Incoming":
			cond += " and master_type = 'Customer'"
		else:
			cond += " and master_type = 'Supplier'"

		party_accounts = frappe.db.sql_list("""select name from `tabAccount`
			where ifnull(master_name, '')!='' and docstatus < 2 %s""" % cond)

	if party_accounts:
		conditions += " and jvd.account in (%s)" % (", ".join(['%s']*len(party_accounts)))
	else:
		msgprint(_("No Customer or Supplier Accounts found"), raise_exception=1)

	if filters.get("from_date"): conditions += " and jv.posting_date >= '%s'" % filters["from_date"]
	if filters.get("to_date"): conditions += " and jv.posting_date <= '%s'" % filters["to_date"]

	return conditions, party_accounts

def get_entries(filters):
	conditions, party_accounts = get_conditions(filters)
	entries =  frappe.db.sql("""select jv.name, jvd.account, jv.posting_date,
		jvd.against_voucher, jvd.against_invoice, jvd.debit, jvd.credit,
		jv.cheque_no, jv.cheque_date, jv.remark
		from `tabJournal Voucher Detail` jvd, `tabJournal Voucher` jv
		where jvd.parent = jv.name and jv.docstatus=1 %s order by jv.name DESC""" %
		(conditions), tuple(party_accounts), as_dict=1)

	return entries

def get_invoice_posting_date_map(filters):
	invoice_posting_date_map = {}
	if filters.get("payment_type") == "Incoming":
		for t in frappe.db.sql("""select name, posting_date from `tabSales Invoice`"""):
			invoice_posting_date_map[t[0]] = t[1]
	else:
		for t in frappe.db.sql("""select name, posting_date from `tabPurchase Invoice`"""):
			invoice_posting_date_map[t[0]] = t[1]

	return invoice_posting_date_map