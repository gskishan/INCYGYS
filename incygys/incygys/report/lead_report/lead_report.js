frappe.query_reports["Lead DB Report"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_start(),  // Optional: Current month's start date
            "reqd": 1 // Required field
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_end(),  // Optional: Current month's end date
            "reqd": 1 // Required field
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
            ], // Defined options for your custom lead status
            "default": "Potential" // Optional default value
        }
    ]
};
