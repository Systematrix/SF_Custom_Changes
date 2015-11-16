// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Voided Check"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname":"account",
			"label": __("Bank Account"),
			"fieldtype": "Link",
                        "default": "Wells Fargo Checking - SF",
			"options": "Account",
			"get_query": function() {
				return {
					"query": "erpnext.controllers.queries.get_account_list", 
					"filters": [
						['Account', 'account_type', 'in', 'Bank, Cash'],
						['Account', 'group_or_ledger', '=', 'Ledger'],
					]
				}
			}
		},
		{
			"fieldname":"include_cancelled_jv",
			"label": __("Show Cancelled JV#"),
			"fieldtype": "Check",
			"default": 1
		},
	]
}