// Copyright (c) 2013, Systematrix and contributors
// For license information, please see license.txt

frappe.query_reports["Custom Stock Qty"] = {
	"filters": [
		{
			"fieldname":"warehouse",
			"label": __("Warehouse"),
			"fieldtype": "Link",
			"options": "Warehouse"
		},
		{
			"fieldname":"item_code",
			"label": __("Item"),
			"fieldtype": "Link",
			"options": "Item"
		}
	]
}
