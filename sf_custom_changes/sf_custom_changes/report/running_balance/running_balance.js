// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Running Balance"] = {
	"filters": [
                 {
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("company"),
			"reqd": 1
		},
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
			"options": "Account",
                        "default": "Wells Fargo Checking - SF",
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
	]
}
