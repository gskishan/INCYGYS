import frappe

def create_opportunity_on_lead_update(doc, method):
    if doc.status == "Interested":
        try:
            # Create a new Opportunity document
            opportunity = frappe.get_doc({
                "doctype": "Opportunity",
                "opportunity_from": "Lead",
                "party_name": doc.first_name,
                # "lead": doc.name,
                "custom_construction_status": doc.custom_construction_status,
                "source": doc.source,
                "contact_person": doc.custom_supervisor_name,
                "contact_mobile": doc.custom_supervisor_phone,
                # "contact_email": doc.email_id,
                "company": doc.custom_sales_organization,
                "transaction_date": frappe.utils.nowdate(),
            })
            opportunity.insert(ignore_permissions=True)
            frappe.db.commit()
            frappe.msgprint(f"Opportunity created for Lead {doc.lead_name}")
        except Exception as e:
            frappe.log_error(message=str(e), title="Opportunity Creation Error")
            frappe.throw(f"Failed to create Opportunity: {str(e)}")

# Attach the function to the Lead doctype's on_update event
frappe.get_hooks('doc_events')['Lead'] = {'on_update': create_opportunity_on_lead_update}
