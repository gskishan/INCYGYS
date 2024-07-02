import frappe
from erpnext.crm.doctype.opportunity.opportunity import Opportunity

@frappe.whitelist()
def create_opportunity_on_lead_status(doc, method):
    # Check if the lead status is 'Interested'
    if doc.custom_lead_status == "Interested":
        # Create a new Opportunity
        opportunity = frappe.new_doc("Opportunity")
        opportunity.party_name = lead.name
        opportunity.custom_source_type = lead.custom_source_type
        opportunity.contact_email = lead.email_id
        opportunity.contact_mobile = lead.mobile_no
        opportunity.opportunity_from = "Lead"
        opportunity.company = lead.custom_sales_organization

        # Save the Opportunity
        opportunity.insert()
        frappe.db.commit()

        # Optionally, you can link this opportunity back to the lead
        doc.opportunity = opportunity.name
        doc.save()
