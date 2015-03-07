# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import logging
import string
import datetime
import re
import json

from frappe import _
from frappe.utils import cstr, validate_email_add, cint, comma_and
from frappe.model.document import Document

_logger = logging.getLogger(frappe.__name__)

@frappe.whitelist(allow_guest=True)

def validate_bill_no(self, method):
		if self.bill_no:
			# validate email is unique
			bill_list = frappe.db.sql("""select name from `tabPurchase Invoice` where bill_no=%s and docstatus = 1""",
				self.bill_no)
			_logger.info("doc validate server vat is {0}".format(self.bill_no))
			if len(bill_list) > 0:
				items = [e[0] for e in bill_list if e[0]!=self.name]
				frappe.throw(_("Supplier Invoice Number must be unique. Current Supplier Invoice Number already exists for {0}").format(comma_and(items)))
