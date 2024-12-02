frappe.query_reports["Custom Lead Report"] = {
    filters: [
        {
            fieldname: "custom_lead_status",
            label: __("Status"),
            fieldtype: "Select",
            default: "Open",
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
        }
    ]
};
