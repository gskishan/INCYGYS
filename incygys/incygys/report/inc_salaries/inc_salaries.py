# Copyright (c) 2024, gskishan and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	cond=data_condtion(filters)
	sql="""select "CODEBEES" client_code,"RPAY" product_code,"NEFT" Payment_Type,"" Payment_Ref_No,posting_date,"" instrument_date,
"05522000003410" Dr_Ac_No,net_pay as amount,"M" Bank_Code_Indicator,"" Beneficiary_Code, upper(s.custom_account_name) as Beneficiary_Name,"" Beneficiary_Bank,
custom_ifsc_code ,bank_account_no Beneficiary_Acc_No,
 CONCAT(
	UPPER(DATE_FORMAT(start_date, '%M')), 
	' SALARIES ', 
	DATE_FORMAT(start_date, '%Y')
) AS Debit_Narration,
CONCAT(
	'SALARY FOR THE MONTH OF ', 
	UPPER(DATE_FORMAT(start_date, '%M')), 
	' ', 
	DATE_FORMAT(start_date, '%Y')
) AS Credit_Narration




 from `tabSalary Slip` s inner join `tabEmployee` e on  s.employee=e.name
 where s.docstatus=1 and s.bank_name!="Kotak Mahindra bank" {0} """.format(cond)
	data =frappe.db.sql(sql,as_dict=1)
	columns = get_columns()

	return columns, data



def data_condtion(filters):
	condition=" "
	if filters.get("from_date") and filters.get("to_date"):
		condition=condition+"and posting_date BETWEEN '{0}' AND '{1}' ".format(filters.get("from_date") ,filters.get("to_date"))
	if filters.get("company"):
		condition=condition+"and s.company='{0}' ".format(filters.get("company"))
	if filters.get("employee"):
		condition=condition+"and s.employee='{0}' ".format(filters.get("employee"))

	return condition


def get_columns():
	columns=[]

	columns+= [
		{
			"fieldname": "client_code",
			"fieldtype": "Data",
			"label": "Client_Code",
			'width': 120
		},
		{
			"fieldname": "product_code",
			"fieldtype": "Data",
			"label": "Product_Code",
			'width': 120
		},
		{
	 		'fieldname': 'Payment_Type',
			'label':('Payment_Type'),
			"fieldtype": "Data",
			'width': 170
		},
		{
	 		'fieldname': 'Payment_Ref_No.',
			'label':('Payment_Ref_No.'),
			"fieldtype": "Data",
			'width': 170
		},
		{
			'fieldname': "posting_date",
			'label': ('Payment_Date'),
			'fieldtype': 'Date',
			'width': 170
		},
		{
	 		'fieldname': 'instrument_date',
			'label':('Instrument Date'),
			"fieldtype": "Data",
			'width': 170
		},
		{
	 		'fieldname': 'Dr_Ac_No',
			'label':('Dr_Ac_No'),
			"fieldtype": "Data",
			'width': 170
		},{
	 		'fieldname': 'amount',
			'label':('Amount'),
			"fieldtype": "Float",
			'width': 170
		},{
	 		'fieldname': 'Bank_Code_Indicator',
			'label':('Bank_Code_Indicator'),
			"fieldtype": "Data",
			'width': 170
		},
		{
			'label': _('Beneficiary_Code'),
			'fieldname':  "Beneficiary_Code",
			'fieldtype': 'Data',
			'width': 160
		},
			{
			'label': _('Beneficiary_Name'),
			'fieldname':  "Beneficiary_Name",
			'fieldtype': 'Data',
			'width': 160
		},
			{
			'label': _('Beneficiary_Bank'),
			'fieldname':  "Beneficiary_Bank",
			'fieldtype': 'Data',
			'width': 160
		},
			{
			'label': _('Beneficiary_Branch / IFSC Code'),
			'fieldname':  "custom_ifsc_code",
			'fieldtype': 'Data',
			'width': 160
		},
			{
			'label': _('Beneficiary_Acc_No'),
			'fieldname':  "Beneficiary_Acc_No",
			'fieldtype': 'Data',
			'width': 160
		},
		{
			'label': _('Location'),
			'fieldname':  "Location",
			'fieldtype': 'Data',
			'width': 120
		},
		{
			'label': _('Print_Location'),
			'fieldname':  "Print_Location",
			'fieldtype': 'Data',
			'width': 120
		},{
			'label': _('Instrument_Number'),
			'fieldname':  "Instrument_Number",
			'fieldtype': 'Data',
			'width': 120
		},
		{
			"label": _("Ben_Add1"),
			"fieldname": "Ben_Add1",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Ben_Add2"),
			"fieldname": "Ben_Add2",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Ben_Add3"),
			"fieldname": "Ben_Add3",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Ben_Add4"),
			"fieldname": "Ben_Add4",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Beneficiary_Email"),
			"fieldname": "Beneficiary_Email",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Beneficiary_Mobile"),
			"fieldname": "Beneficiary_Mobile",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Debit_Narration"),
			"fieldname": "Debit_Narration",
			"fieldtype": "Data",
			"width": 280
		},
		{
			"label": _("Credit_Narration"),
			"fieldname": "Credit_Narration",
			"fieldtype": "Data",
			"width": 310
		},
		{
			"label": _("Payment Details 1"),
			"fieldname": "Payment_Details_1",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Payment Details 2"),
			"fieldname": "Payment_Details_2",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Payment Details 3"),
			"fieldname": "Payment_Details_3",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Payment Details 4"),
			"fieldname": "Payment_Details_4",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 1"),
			"fieldname": "Enrichment_1",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 2"),
			"fieldname": "Enrichment_2",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 3"),
			"fieldname": "Enrichment_3",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 4"),
			"fieldname": "Enrichment_4",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 5"),
			"fieldname": "Enrichment_5",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 6"),
			"fieldname": "Enrichment_6",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 7"),
			"fieldname": "Enrichment_7",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 8"),
			"fieldname": "Enrichment_8",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 9"),
			"fieldname": "Enrichment_9",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 10"),
			"fieldname": "Enrichment_10",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 11"),
			"fieldname": "Enrichment_11",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 12"),
			"fieldname": "Enrichment_12",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 13"),
			"fieldname": "Enrichment_13",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 14"),
			"fieldname": "Enrichment_14",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 15"),
			"fieldname": "Enrichment_15",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 16"),
			"fieldname": "Enrichment_16",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 17"),
			"fieldname": "Enrichment_17",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 18"),
			"fieldname": "Enrichment_18",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 19"),
			"fieldname": "Enrichment_19",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Enrichment 20"),
			"fieldname": "Enrichment_20",
			"fieldtype": "Data",
			"width": 120
		}
			
			
		
	]



	
	return columns
