import frappe

def execute(filters=None):
    columns, data = [], []

    columns = get_columns()
    data = get_data(filters)

    return columns, data

def get_columns():
    return [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 150},
        {"label": "Open Enquiries", "fieldname": "open_count", "fieldtype": "Int", "width": 150},
        {"label": "Interested Enquiries", "fieldname": "interested_count", "fieldtype": "Int", "width": 150},
        {"label": "Quotations", "fieldname": "quotation_count", "fieldtype": "Int", "width": 150},
        {"label": "Do Not Contact", "fieldname": "do_not_contact_count", "fieldtype": "Int", "width": 150}
    ]

def get_data(filters):
    data = []

    employees = frappe.get_all('Employee', fields=['name', 'employee_name'])
    
    for employee in employees:
        open_count = frappe.db.count('Enquiry', {'enquiry_owner': employee.name, 'status': 'Open'})
        interested_count = frappe.db.count('Enquiry', {'enquiry_owner': employee.name, 'status': 'Interested'})
        quotation_count = frappe.db.count('Enquiry', {'enquiry_owner': employee.name, 'status': 'Quotation'})
        do_not_contact_count = frappe.db.count('Enquiry', {'enquiry_owner': employee.name, 'status': 'Do Not Contact'})

        row = {
            "employee": employee.name,
            "open_count": open_count,
            "interested_count": interested_count,
            "quotation_count": quotation_count,
            "do_not_contact_count": do_not_contact_count
        }
        data.append(row)

    return data
