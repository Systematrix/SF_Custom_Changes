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
					"is_query_report": True,
					"name": "Sales Invoice Custom Report",
					"doctype": "Sales Invoice",
                                        "description": _("Custom Report"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase Invoice Custom Report",
					"doctype": "Purchase Invoice",
                                        "description": _("Custom Report"),
				},
				{
					"type": "report",
					"name": "Accounts Receivable - Concise",
					"doctype": "Sales Invoice",
					"is_query_report": True,
                                        "description": _("Concise Report"),
				},
				{
					"type": "report",
					"name": "Accounts Payable - Concise",
					"doctype": "Purchase Invoice",
					"is_query_report": True,
                                        "description": _("Concise Report"),
				},
			        {
					"type": "report",
					"name": "Custom Payment Period Based On Invoice Date",
					"doctype": "Journal Voucher",
					"is_query_report": True,
                                        "description": _("Custom Report"),
				},
				
			]
		},
                {
			"label": _("Tools"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Custom Bank Reconciliation",
					"description": _("Update bank payment dates with journals.")
				},
			]
		},
	]
