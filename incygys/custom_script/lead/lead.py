import frappe
from erpnext.crm.doctype.opportunity.opportunity import Opportunity

@frappe.whitelist()
def create_opportunity_on_lead_status(doc, method):
    if doc.custom_lead_status == "Interested" and not doc.custom_opportunity:
        opportunity = frappe.new_doc("Opportunity")
        opportunity.party_name = doc.name
        opportunity.custom_source_type = doc.custom_source_type
        opportunity.custom_salutation = doc.salutation
        opportunity.custom_city_name = doc.custom_city_name
        opportunity.custom_emails = doc.custom_email
        opportunity.custom_mobiles = doc.custom_mobile_numbers
        opportunity.opportunity_from = "Lead"
        opportunity.company = doc.custom_sales_organization
        opportunity.custom_property_type = doc.custom_property_type
        opportunity.custom_sq_ft = doc.custom_sq_ft
        opportunity.custom_opportunity_name = doc.lead_name
        opportunity.opportunity_owner = doc.lead_owner
        opportunity.custom_source_type = doc.custom_source_type
        opportunity.custom_construction_type = doc.custom_construction_type
        opportunity.expected_closing = doc.custom_requirement_stage_date
        opportunity.country = doc.country
        opportunity.custom_state_copy = doc.custom_state_copy
        opportunity.city = doc.city
        opportunity.custom_address = doc.custom_address
        opportunity.custom_supervisor_name = doc.custom_supervisor_name
        opportunity.custom_supervisor_phone = doc.custom_supervisor_phone
        opportunity.contact_email = doc.email_id
        opportunity.save()
        doc.db_set("custom_opportunity", opportunity.name, update_modified=False)
        frappe.msgprint(f'Opportunity {opportunity.name} has been created for Lead {doc.name}')
