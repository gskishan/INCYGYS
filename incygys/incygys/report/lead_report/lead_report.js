frappe.query_reports["Lead Report"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_start(),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_end(),
            "reqd": 1
        },
        {
            "fieldname": "custom_lead_status",
            "label": __("Custom Lead Status"),
            "fieldtype": "Select",
            "options": [
                "Potential",
                "Interested",
                "Unresponded",
                "Not-Interested"
            ],
            "default": "Potential"
        }
    ]
};
