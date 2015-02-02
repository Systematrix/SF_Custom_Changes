app_name = "sf_custom_changes"
app_title = "SF Custom Changes"
app_publisher = "Systematrix"
app_description = "SF Custom App"
app_icon = "icon-book"
app_color = "#589494"
app_email = "info@systematrix.co.in"
app_url = "https://github.com/Systematrix/SF_Custom_Changes"
app_version = "0.0.1"
fixtures = ["Custom Field",
"Property Setter",
"Custom Script",
"Print Format",
"Report"]

doc_events = {
	"Purchase Invoice": {
		"before_save": "sf_custom_changes.sf_acc.purchase.validate_server_vat"
	}
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sf_custom_changes/css/sf_custom_changes.css"
# app_include_js = "/assets/sf_custom_changes/js/sf_custom_changes.js"

# include js, css files in header of web template
# web_include_css = "/assets/sf_custom_changes/css/sf_custom_changes.css"
# web_include_js = "/assets/sf_custom_changes/js/sf_custom_changes.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sf_custom_changes.install.before_install"
# after_install = "sf_custom_changes.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sf_custom_changes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sf_custom_changes.tasks.all"
# 	],
# 	"daily": [
# 		"sf_custom_changes.tasks.daily"
# 	],
# 	"hourly": [
# 		"sf_custom_changes.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sf_custom_changes.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sf_custom_changes.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sf_custom_changes.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "sf_custom_changes.event.get_events"
# }

