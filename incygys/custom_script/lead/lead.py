import frappe

@frappe.whitelist()
def create_opportunity_from_lead(lead_name):
    try:
        lead = frappe.get_doc("Lead", lead_name)
        if lead.custom_lead_status == "Interested":
            opportunity = frappe.new_doc("Opportunity")
            opportunity.party_name = lead.name
            opportunity.custom_source_type = lead.custom_source_type
            opportunity.contact_email = lead.email_id
            opportunity.contact_mobile = lead.mobile_no
            opportunity.opportunity_from = "Lead"
            opportunity.insert()
            frappe.msgprint(f"Opportunity {opportunity.name} created from Lead {lead.name}")
            return opportunity
    except frappe.DoesNotExistError:
        frappe.msgprint(f"Lead {lead_name} not found")
    except Exception as e:
        frappe.log_error(f"An error occurred while creating an opportunity from lead {lead_name}: {str(e)}")

def lead_after_save(doc, method):
    if doc.custom_lead_status == "Interested":
        create_opportunity_from_lead(doc.name)
