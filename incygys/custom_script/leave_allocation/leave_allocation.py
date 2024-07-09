import frappe
from frappe.utils import today

@frappe.whitelist()
def allocate_leaves_on_employee_creation(doc, method):
    leave_types = ['Casual Leave', 'Privilege Leave', 'Sick Leave']
    allocation_data = {
        'Casual Leave': {'total_leaves_allocated': 0},  # Example allocation, adjust as needed
        'Privilege Leave': {'total_leaves_allocated': 0},  # Example allocation, adjust as needed
        'Sick Leave': {'total_leaves_allocated': 0}  # Example allocation, adjust as needed
    }
    to_date = '2024-12-31'

    for leave_type in leave_types:
        leave_allocation = frappe.new_doc("Leave Allocation")
        leave_allocation.employee = doc.name
        leave_allocation.leave_type = leave_type
        leave_allocation.from_date = today()
        leave_allocation.to_date = to_date  # Set to appropriate end date, e.g., end of the fiscal year
        leave_allocation.total_leaves_allocated = allocation_data[leave_type]['total_leaves_allocated']
        leave_allocation.submit()  # Leave Allocation is a submitted document

    frappe.msgprint(f'Leaves have been allocated for Employee {doc.name}')
