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
					"name": "For Wells Fargo",
					"doctype": "GL Entry",
                                        "description": _("Running Balance"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "For SquareUP",
					"doctype": "GL Entry",
                                        "description": _("Running Balance"),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "For USBank",
					"doctype": "GL Entry",
                                        "description": _("Running Balance"),
				},
				
			]
		},
	]
