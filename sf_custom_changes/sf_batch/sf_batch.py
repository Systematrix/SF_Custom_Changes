# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import logging

from frappe.utils import getdate, flt,validate_email_add, cint
from frappe.model.naming import make_autoname
from frappe import throw, _, msgprint
import frappe.permissions
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


_logger = logging.getLogger(frappe.__name__)

def get_actual_batch_qty(batch_no,warehouse,item_code):
        actual_batch_qty = 0
        if batch_no:
            actual_batch_qty = flt(frappe.db.sql("""select sum(actual_qty)
				from `tabStock Ledger Entry`
				where warehouse=%s and item_code=%s and batch_no=%s""",
				(warehouse, item_code, batch_no))[0][0])
        msgprint(_("Available Qty of selected batch is: {0}").format(actual_batch_qty))
        return actual_batch_qty

@frappe.whitelist(allow_guest=True)
def get_batch_qty(batch_no,warehouse,item_code):
	ret = {}
        actual_batch_qty = get_actual_batch_qty(batch_no,warehouse,item_code)
	if batch_no:
		ret = {'actual_batch_qty': actual_batch_qty}
	return ret
