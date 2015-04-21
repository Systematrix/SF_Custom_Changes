// Copyright (c) 2013, Systematrix and contributors
// License: GNU General Public License v3, please see license.txt

frappe.query_reports["Batch-Wise Balance History Report"] = {
	"filters": [
                {
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": sys_defaults.year_start_date,
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.get_today()
		}
	]
}
