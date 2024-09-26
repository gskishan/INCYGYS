import frappe
from erpnext.crm.doctype.opportunity.opportunity import Opportunity

def duplicate_check(doc, method):
    mobile_no = str(doc.custom_mobile_numbers).replace("+91", "").replace("-", "").strip()
    sql = """SELECT * FROM `tabLead` WHERE REPLACE(REPLACE(mobile_no, '+91', ''), '-', '') = %s AND name != %s"""
    data = frappe.db.sql(sql, (mobile_no, doc.name), as_dict=True)

    email_sql = """SELECT * FROM `tabLead` WHERE custom_email = %s AND name != %s"""
    email_data = frappe.db.sql(email_sql, (doc.custom_email, doc.name), as_dict=True)

    if data:
        frappe.errprint(data)
        frappe.throw(f"Duplicate mobile number {mobile_no} already linked to <b>{data[0].custom_owner_name}</b>")
    if email_data:
        frappe.errprint(email_data)
        frappe.throw(f"Duplicate email {doc.custom_email} already linked to <b>{email_data[0].custom_owner_name}</b>")

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
        
        for product in doc.custom_list_of_products:
            opportunity.append('custom_list_of_products', {
                'list_of_products': product.list_of_products,
            })
        opportunity.save()
        doc.db_set("custom_opportunity", opportunity.name, update_modified=False)
        frappe.msgprint(f'Opportunity {opportunity.name} has been created for Lead {doc.name}')
