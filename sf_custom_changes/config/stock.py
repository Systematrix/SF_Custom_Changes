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
					"name": "Custom Stock Ledger",
					"doctype": "Item",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Custom Stock Balance",
					"doctype": "Warehouse"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Custom Stock Balance - Concise",
					"doctype": "Warehouse"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Custom Stock Projected Qty",
					"doctype": "Item"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Balance by Batch",
					"doctype": "Stock Ledger Entry"
				},
				
			]
		},
	]
