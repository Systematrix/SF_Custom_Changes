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
					"name": "Check Register",
					"doctype": "Journal Voucher",
                                        "description": _("Check Register"),
				},
                                {
					"type": "report",
					"is_query_report": True,
					"name": "Consolidated Banks Report",
					"doctype": "Journal Voucher",
                                        "description": _("Consolidated Banks Report"),
				},
				{
					"type": "report",
					"name": "Accounts Receivable - Concise",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Accounts Payable - Concise",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
				
			]
		},
	]
