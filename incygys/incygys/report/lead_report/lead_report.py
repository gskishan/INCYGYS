import frappe
from frappe import _

def execute(filters=None):
    # Ensure filters are passed to avoid issues
    if not filters:
        filters = {}

    query = """
    SELECT
        `tabLead`.`custom_sales_organization` AS "Sales Organization",
        `tabLead`.`lead_name` AS "Lead Name",
        `tabLead`.`custom_mobile_numbers` AS "Mobile Numbers",
        `tabLead`.`custom_email` AS "Email",
        `tabLead`.`country` AS "Country",
        `tabLead`.`custom_state_copy` AS "State",
        `tabLead`.`custom_city_name` AS "City",
        `tabLead`.`custom_address` AS "Address",
        `tabLead`.`custom_lead_status` AS "Lead Status",
        `tabLead`.`custom_source_type` AS "Source Type",
        `tabLead`.`custom_architect_is` AS "Architect",
        `tabLead`.`owner` AS "Lead Owner",
        `tabLead`.`custom_owner_name` AS "Owner Name",
        `tabLead`.`custom_property_type` AS "Property Type",
        `tabLead`.`custom_sq_ft` AS "Size sq ft",
        `tabLead`.`custom_requirement_stage_date` AS "Requirement Stage Date",
        `tabLead`.`custom_supervisor_name` AS "Supervisor Name",
        `tabLead`.`custom_supervisor_phone` AS "Supervisor Phone",
        `tabLead`.`email_id` AS "Email ID",
        `tabLead`.`creation` AS "Creation Date",
        `tabLead`.`modified` AS "Last Modified",
        CASE 
            WHEN `tabLead`.`custom_source_type` = 'Architect' THEN `tabLead`.`custom_name`
            WHEN `tabLead`.`custom_source_type` = 'Contractor' THEN `tabLead`.`custom_contractor_name`
            WHEN `tabLead`.`custom_source_type` = 'Dealer' THEN `tabLead`.`custom_dealer_name`
            WHEN `tabLead`.`custom_source_type` = 'Others' THEN `tabLead`.`custom_reference_name`
            WHEN `tabLead`.`custom_source_type` = 'Consultant' THEN `tabLead`.`custom_consultant_names`
            WHEN `tabLead`.`custom_source_type` = 'Event/Exhibition' THEN `tabLead`.`custom_eventexhibition_type`
            WHEN `tabLead`.`custom_source_type` = 'Builder' THEN `tabLead`.`custom_builder_name`
            ELSE NULL
        END AS "Lead Source Name"
    FROM
        `tabLead`
    WHERE
        `tabLead`.`custom_lead_status` = %(custom_lead_status)s
        AND `tabLead`.`creation` BETWEEN %(from_date)s AND %(to_date)s
    ORDER BY
        `tabLead`.`creation` DESC
    """
    # Execute query with filters
    data = frappe.db.sql(query, filters, as_dict=True)
    # Define columns for report
    columns = [
        {"fieldname": "Sales Organization", "label": _("Sales Organization"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Lead Name", "label": _("Lead Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Mobile Numbers", "label": _("Mobile Numbers"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Email", "label": _("Email"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Country", "label": _("Country"), "fieldtype": "Data", "width": 120},
        {"fieldname": "State", "label": _("State"), "fieldtype": "Data", "width": 120},
        {"fieldname": "City", "label": _("City"), "fieldtype": "Data", "width": 120},
        {"fieldname": "Address", "label": _("Address"), "fieldtype": "Data", "width": 200},
        {"fieldname": "Lead Status", "label": _("Lead Status"), "fieldtype": "Select", "width": 120},
        {"fieldname": "Source Type", "label": _("Source Type"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Architect", "label": _("Architect"), "fieldtype": "Data", "width": 100},
        {"fieldname": "Lead Owner", "label": _("Lead Owner"), "fieldtype": "Link", "options": "User", "width": 120},
        {"fieldname": "Owner Name", "label": _("Owner Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Property Type", "label": _("Property Type"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Size sq ft", "label": _("Size sq ft"), "fieldtype": "Float", "width": 120},
        {"fieldname": "Requirement Stage Date", "label": _("Requirement Stage Date"), "fieldtype": "Date", "width": 120},
        {"fieldname": "Supervisor Name", "label": _("Supervisor Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Supervisor Phone", "label": _("Supervisor Phone"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Email ID", "label": _("Email ID"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Creation Date", "label": _("Creation Date"), "fieldtype": "Date", "width": 120},
        {"fieldname": "Last Modified", "label": _("Last Modified"), "fieldtype": "Date", "width": 120},
        {"fieldname": "Lead Source Name", "label": _("Lead Source Name"), "fieldtype": "Data", "width": 150}
    ]
    return columns, data
