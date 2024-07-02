from hrms.hr.doctype.attendance.attendance import Attendance
import frappe
from frappe import _
from frappe.utils import (
	format_date,
	getdate
)
class CustomAttendence(Attendance):
	def check_leave_record(self):
		frappe.errprint("working001")
		LeaveApplication = frappe.qb.DocType("Leave Application")
		leave_record = (
			frappe.qb.from_(LeaveApplication)
			.select(
				LeaveApplication.leave_type,
				LeaveApplication.half_day,
				LeaveApplication.half_day_date,
				LeaveApplication.name,
			)
			.where(
				(LeaveApplication.employee == self.employee)
				& (self.attendance_date >= LeaveApplication.from_date)
				& (self.attendance_date <= LeaveApplication.to_date)
				& (LeaveApplication.status == "Approved")
				& (LeaveApplication.docstatus == 1)
			)
		).run(as_dict=True)

		if leave_record:
			half_day_count=0
			for d in leave_record:
				self.leave_type = d.leave_type
				self.leave_application = d.name
				if d.half_day_date == getdate(self.attendance_date):
					half_day_count+1
			if half_day_count == 2:
				self.status = "On Leave"
				frappe.msgprint(
					_("Employee {0} is on Leave on {1} due to two half days").format(
						self.employee, format_date(self.attendance_date)
					)
				)
			elif half_day_count == 1:
				self.status = "Half Day"
				frappe.msgprint(
					_("Employee {0} on Half day on {1}").format(
						self.employee, format_date(self.attendance_date)
					)
				)
			else:
				self.status = "On Leave"
				frappe.msgprint(
					_("Employee {0} is on Leave on {1}").format(
						self.employee, format_date(self.attendance_date)
					)
				)

		if self.status in ("On Leave", "Half Day"):
			if not leave_record:
				frappe.msgprint(
					_("No leave record found for employee {0} on {1}").format(
						self.employee, format_date(self.attendance_date)
					),
					alert=1,
				)
		elif self.leave_type:
			self.leave_type = None
			self.leave_application = None
