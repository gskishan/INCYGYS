frappe.query_reports["Opportunity Report"] = {
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
            "fieldname": "ststus",
            "label": __("Opportunity Status"),
            "fieldtype": "Select",
            "options": [
                "Quotation",
                "Converted",
                "Lost"
            ],
            "default": "Quotation"
        }
    ]
};
