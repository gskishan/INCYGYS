import frappe

def duplicate_check_in_opportunity(doc, method):
    if doc.is_new():
        # Check for duplicate mobile numbers in Opportunity
        opportunity_mobile_check = frappe.db.exists(
            "Opportunity", {"custom_mobiles": doc.custom_mobiles}
        )
        if opportunity_mobile_check:
            duplicate_opportunity = frappe.get_doc(
                "Opportunity", opportunity_mobile_check
            )
            frappe.throw(
                f"Duplicate mobile number {doc.custom_mobiles} already linked to Opportunity <b>{duplicate_opportunity.opportunity_owner}</b>"
            )

        # Check for duplicate emails in Opportunity
        opportunity_email_check = frappe.db.exists(
            "Opportunity", {"custom_emails": doc.custom_emails}
        )
        if opportunity_email_check:
            duplicate_opportunity = frappe.get_doc(
                "Opportunity", opportunity_email_check
            )
            frappe.throw(
                f"Duplicate email {doc.custom_emails} already linked to Opportunity <b>{duplicate_opportunity.opportunity_owner}</b>"
            )
