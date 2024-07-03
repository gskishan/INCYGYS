from hrms.hr.doctype.leave_application.leave_application import LeaveApplication
import frappe
from frappe import _
from frappe.utils import (
	format_date,
	getdate
)
class CustomLeaveApplication(LeaveApplication):
  def create_or_update_attendance(self, attendance_name, date):
		status = (
			"Half Day" if self.half_day_date and getdate(date) == getdate(self.half_day_date) else "On Leave"
		)

		if attendance_name:
			# update existing attendance, change absent to on leave
			doc = frappe.get_doc("Attendance", attendance_name)
			doc.db_set({"status": status, "leave_type": self.leave_type, "leave_application": self.name})
		else:
			# make new attendance and submit it
			doc = frappe.new_doc("Attendance")
			doc.employee = self.employee
			doc.employee_name = self.employee_name
			doc.attendance_date = date
			doc.company = self.company
			doc.leave_type = self.leave_type
			doc.leave_application = self.name
			doc.status = status
			doc.flags.ignore_validate = True
			doc.insert(ignore_permissions=True)
			doc.submit()

