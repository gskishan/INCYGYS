import frappe
from erpnext.crm.doctype.opportunity.opportunity import Opportunity

@frappe.whitelist()
def create_opportunity_on_lead_status(doc, method):
    if doc.custom_lead_status == "Interested":
        opportunity = frappe.new_doc("Opportunity")
        opportunity.party_name = doc.name
        opportunity.custom_source_type = doc.custom_source_type
        opportunity.contact_email = doc.email_id
        opportunity.contact_mobile = doc.mobile_no
        opportunity.opportunity_from = "Lead"
        opportunity.company = doc.custom_sales_organization

        opportunity.insert()
        frappe.db.commit()

        
        doc.opportunity = opportunity.name
        doc.save(ignore_version=True)

        frappe.msgprint(f'Opportunity {opportunity.name} has been created for Lead {doc.name}')
