def execute(filters=None):
    query = """
    SELECT
        `tabLead`.`first_name` AS "First Name",
        `tabLead`.`last_name` AS "Last Name",
        `tabLead`.`city` AS "City",
        `tabLead`.`custom_state_name` AS "State",
        `tabLead`.`custom_mobile_numbers` AS "Mobile",
        `tabLead`.`custom_lead_status` AS "Lead Status",
        `tabLead`.`custom_owner_name` AS "Owner Name",
        `tabLead`.`custom_source_type` AS "Lead Source",
        CASE 
            WHEN `tabLead`.`custom_source_type` = 'Architect' THEN `tabLead`.`custom_name`
            WHEN `tabLead`.`custom_source_type` = 'Contractor' THEN `tabLead`.`custom_contractor_name`
            WHEN `tabLead`.`custom_source_type` = 'Dealer' THEN `tabLead`.`custom_dealer_name`
            WHEN `tabLead`.`custom_source_type` = 'Others' THEN `tabLead`.`custom_reference_name`
            WHEN `tabLead`.`custom_source_type` = 'Consultant' THEN `tabLead`.`custom_consultant_names`
            WHEN `tabLead`.`custom_source_type` = 'Event/Exhibition' THEN `tabLead`.`custom_eventexhibition_type`
            WHEN `tabLead`.`custom_source_type` = 'Builder' THEN `tabLead`.`custom_builder_name`
            ELSE NULL
        END AS "Lead Source Name",
        `tabLead`.`custom_property_type` AS "Property Type",
        `tabLead`.`custom_sq_ft` AS "Size sq ft",
        `tabLead`.`custom_requirement_stage_date` AS "Requirement Stage Date",
        `tabLead`.`name` AS "Lead ID"
    FROM
        `tabLead`
    WHERE
        `tabLead`.`custom_lead_status` = %(status)s
        AND `tabLead`.`creation` BETWEEN %(from_date)s AND %(to_date)s
    ORDER BY
        `tabLead`.`creation` DESC
    """
    data = frappe.db.sql(query, filters, as_dict=True)
    return [], data
