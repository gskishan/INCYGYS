import frappe
from frappe import _

def execute(filters=None):
    # Ensure filters are passed to avoid issues
    if not filters:
        filters = {}

    query = """
    SELECT
        `tabOpportunity`.`custom_opportunity_name` AS "First Name",
        `tabOpportunity`.`custom_last_name` AS "Last Name",
        `tabOpportunity`.`city` AS "City",
        `tabOpportunity`.`custom_state_copy` AS "State",
        `tabOpportunity`.`custom_mobiles` AS "Mobile",
        `tabOpportunity`.`status` AS "Opportunity Status",
        `tabOpportunity`.`owner` AS "Opportunity Owner",
        `tabOpportunity`.`opportunity_from` AS "Opportunity Source",
        `tabOpportunity`.`custom_property_type` AS "Property Type",
        `tabOpportunity`.`custom_sq_ft` AS "Sq Ft",
        `tabOpportunity`.`opportunity_amount` AS "Opportunity Value",
        `tabOpportunity`.`expected_closing` AS "Requirement Stage Date",
        `tabOpportunity`.`custom_revised_closing_date` AS "Revised Requirement Stage Date",
        `tabOpportunity`.`custom_supervisor_name` AS "Site Supervisor Name",
        `tabOpportunity`.`custom_supervisor_phone` AS "Site Supervisor Mobile",
        `tabOpportunity`.`name` AS "Opp ID",
        `tabOpportunity`.`creation` AS "Creation Date",
        `tabOpportunity`.`modified` AS "Last Modified"
    FROM
        `tabOpportunity`
    WHERE
        `tabOpportunity`.`status` = %(status)s
        AND `tabOpportunity`.`creation` BETWEEN %(from_date)s AND %(to_date)s
    ORDER BY
        `tabOpportunity`.`creation` DESC
    """
    # Execute query with filters
    data = frappe.db.sql(query, filters, as_dict=True)
    
    # Define columns for report
    columns = [
        {"fieldname": "First Name", "label": _("First Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Last Name", "label": _("Last Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "City", "label": _("City"), "fieldtype": "Data", "width": 120},
        {"fieldname": "State", "label": _("State"), "fieldtype": "Data", "width": 120},
        {"fieldname": "Mobile", "label": _("Mobile"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Opportunity Status", "label": _("Opportunity Status"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Opportunity Owner", "label": _("Opportunity Owner"), "fieldtype": "Link", "options": "User", "width": 150},
        {"fieldname": "Opportunity Source", "label": _("Opportunity Source"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Property Type", "label": _("Property Type"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Sq Ft", "label": _("Sq Ft"), "fieldtype": "Float", "width": 120},
        {"fieldname": "Opportunity Value", "label": _("Opportunity Value"), "fieldtype": "Currency", "width": 150},
        {"fieldname": "Requirement Stage Date", "label": _("Requirement Stage Date"), "fieldtype": "Date", "width": 150},
        {"fieldname": "Revised Requirement Stage Date", "label": _("Revised Requirement Stage Date"), "fieldtype": "Date", "width": 150},
        {"fieldname": "Site Supervisor Name", "label": _("Site Supervisor Name"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Site Supervisor Mobile", "label": _("Site Supervisor Mobile"), "fieldtype": "Data", "width": 150},
        {"fieldname": "Opp ID", "label": _("Opp ID"), "fieldtype": "Link", "options": "Opportunity", "width": 150},
        {"fieldname": "Creation Date", "label": _("Creation Date"), "fieldtype": "Date", "width": 150},
        {"fieldname": "Last Modified", "label": _("Last Modified"), "fieldtype": "Date", "width": 150}
    ]
    return columns, data
