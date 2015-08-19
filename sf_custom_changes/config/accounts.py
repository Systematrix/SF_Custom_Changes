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
					"name": "Running Balance",
					"doctype": "Journal Voucher",
                                        "description": _("Running Balance"),
				},
                                {
					"type": "report",
					"is_query_report": True,
					"name": "Consolidated Banks Report",
					"doctype": "Journal Voucher",
                                        "description": _("Consolidated Banks Report"),
				},
				
			]
		},
	]
