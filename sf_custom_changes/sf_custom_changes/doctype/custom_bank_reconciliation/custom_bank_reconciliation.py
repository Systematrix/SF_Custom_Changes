# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt, getdate, nowdate
from frappe import msgprint, _
from frappe.model.document import Document
from datetime import date

class CustomBankReconciliation(Document):
	def get_details(self):
		if not (self.bank_account and self.from_date and self.to_date):
			msgprint("Bank Account, From Date and To Date are Mandatory")
			return
                if self.clearance_date:
                        msgprint(self.clearance_date)

		condition = ""
		if not self.include_reconciled_entries:
			condition = "and ifnull(clearance_date, '') in ('', '0000-00-00')"


		dl = frappe.db.sql("""select t1.name, t1.cheque_no, t1.cheque_date, t2.debit,
				t2.credit, t1.posting_date, t2.against_account, t1.clearance_date
			from
				`tabJournal Voucher` t1, `tabJournal Voucher Detail` t2
			where
				t2.parent = t1.name and t2.account = %s
				and t1.posting_date >= %s and t1.posting_date <= %s and t1.docstatus=1
				and ifnull(t1.is_opening, 'No') = 'No' %s order by t1.posting_date""" %
				('%s', '%s', '%s', condition), (self.bank_account, self.from_date, self.to_date), as_dict=1)

		self.set('entries', [])
		self.total_amount = 0.0
		self.total_reconciled_credit = 0.0
		self.total_reconciled_debit = 0.0
                self.amounts_not_reflected_in_bank = 0.0
                self.expected_balance_as_per_bank = 0.0

		for d in dl:
			nl = self.append('entries', {})
			nl.posting_date = d.posting_date
			nl.voucher_id = d.name
			nl.cheque_number = d.cheque_no
			nl.cheque_date = d.cheque_date
			nl.debit = d.debit
			nl.credit = d.credit
			nl.against_account = d.against_account
			nl.clearance_date = d.clearance_date
			self.total_amount += flt(d.debit) - flt(d.credit)

                        if d.clearance_date: 
                        	self.total_reconciled_debit += flt(d.debit)
                        	self.total_reconciled_credit += flt(d.credit)

                        if not d.clearance_date: 
                        	self.amounts_not_reflected_in_bank += flt(d.debit) - flt(d.credit)
 
                        self.expected_balance_as_per_bank = self.amounts_not_reflected_in_bank - self.system_balance


	def get_clearance_details(self):
		if not (self.clearance_date):
			msgprint("Clearance Date is Mandatory")
			return

		condition = ""


		dl = frappe.db.sql("""select t1.name, t1.cheque_no, t1.cheque_date, t2.debit,
				t2.credit, t1.posting_date, t2.against_account, t1.clearance_date
			from
				`tabJournal Voucher` t1, `tabJournal Voucher Detail` t2
			where
				t2.parent = t1.name and t2.account = %s
				and t1.clearance_date= %s and t1.docstatus=1
				and ifnull(t1.is_opening, 'No') = 'No' %s order by t1.posting_date""" %
				('%s', '%s', condition), (self.bank_account, self.clearance_date), as_dict=1)

		self.set('entries', [])
		self.total_amount = 0.0
		self.total_reconciled_credit = 0.0
		self.total_reconciled_debit = 0.0

		for d in dl:
			nl = self.append('entries', {})
			nl.posting_date = d.posting_date
			nl.voucher_id = d.name
			nl.cheque_number = d.cheque_no
			nl.cheque_date = d.cheque_date
			nl.debit = d.debit
			nl.credit = d.credit
			nl.against_account = d.against_account
			nl.clearance_date = d.clearance_date
			self.total_amount += flt(d.debit) - flt(d.credit)

                        if d.clearance_date: 
                        	self.total_reconciled_debit += flt(d.debit)
                        	self.total_reconciled_credit += flt(d.credit)


	def update_details(self):
		vouchers = []
		for d in self.get('entries'):
			if d.clearance_date:
				if d.cheque_date and getdate(d.clearance_date) < getdate(d.cheque_date):
					frappe.throw(_("Clearance date cannot be before check date in row {0}").format(d.idx))

				frappe.db.set_value("Journal Voucher", d.voucher_id, "clearance_date", d.clearance_date)
				frappe.db.sql("""update `tabJournal Voucher` set clearance_date = %s, modified = %s
					where name=%s""", (d.clearance_date, nowdate(), d.voucher_id))
				vouchers.append(d.voucher_id)

		if vouchers:
			msgprint("Clearance Date updated in: {0}".format(", ".join(vouchers)))
		else:
			msgprint(_("Clearance Date not mentioned"))

	def set_clearance_date(self):
		vouchers = []
		for d in self.get('entries'):
			if not d.clearance_date:
                                d.clearance_date = self.to_date

		msgprint(_("Clearance Date updated "))
