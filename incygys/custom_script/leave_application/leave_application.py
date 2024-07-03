from hrms.hr.doctype.leave_application.leave_application import LeaveApplication
import frappe
from frappe import _
from frappe.utils import (
	format_date,
	getdate
)
class CustomLeaveApplication(LeaveApplication):
	def create_or_update_attendance(self, attendance_name, date):
		frappe.errprint("1onerp")
		status = (
			"Half Day" if self.half_day_date and getdate(date) == getdate(self.half_day_date) else "On Leave"
		)
		sql=""" select *  from  `tabLeave Application` where employee="{0}" and from_date="{1}" and to_date ="{2}" and status="Approved" """.format(self.employee,self.from_date,self.to_date)
		half_day_date_count=0
		for d in (frappe.db.sql(sql,as_dict=True)):
			if d.half_day:
				half_day_date_count+=1


		if attendance_name:
			if status=="Half Day":
				if half_day_date_count==2:
					status="On Leave"

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

