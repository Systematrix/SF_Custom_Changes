from frappe import _

def get_data():
	return [
		{
			"label": _("Custom Reports"),
			"icon": "icon-table",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Custom Sales Partners Commission",
					"doctype": "Sales Invoice",
                                        "description": _("Sales Commission Report"),
				},
                                {
					"type": "report",
					"is_query_report": True,
					"name": "Custom Bank Reconciliation Statement",
					"doctype": "Journal Voucher",
				},
                                {
					"type": "report",
					"is_query_report": True,
					"name": "Custom Bank Clearance Summary",
					"doctype": "Journal Voucher",
				},
				
			]
		},
	]
