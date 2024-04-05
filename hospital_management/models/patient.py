from odoo import models, fields
from datetime import date


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'


    patient_name = fields.Char(string='Patient Name', required=True, translate=True,help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')
    age = fields.Integer(string='Age',help='This field is used to take patient age')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    weight = fields.Float(string='Weight (kg)',help='This field is used to take patient weight',digits=(16,3))
    height = fields.Float(string='Height (ft)',help='This field is used to take patient height',digits=(16,3))
    Diseases=fields.Selection(selection=[('high blood pressure','High Blood Pressure'),('diabetes','Diabetes'),('cholera','Cholera'),('heart attack','Heart Attack')],help='This field show the list of diseases')
    hospital_name = fields.Char(string="Hospital name",size=4)
    # print("Hospital name:", hospital_name)this field take a limited char size=4


    email = fields.Char('Email',help='This field is used to take patient email')
    phone_number = fields.Char(string='Phone Number', size=10,help='This field is used to take patient phone number')
    address = fields.Char('Address',help='This field is used to take patient address')
    is_admitted = fields.Boolean(string='Admitted',help='This field is used to check that patient is admitted or not')
    birthdate = fields.Date('Birthdate', index=True,help='This field is used for birthdate of patient')
    notes = fields.Text('Notes',help='This field is used for notes')
    today = date.today()
    print(today)


    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    timestamp = fields.Date('Timestamp', readonly=True)
    Marital_status = fields.Selection([('married', 'Married'), ('unmarried', 'Unmarried'), ('single', 'Single')], string='Marital Status')

    diagnosis_notes = fields.Html(string='Diagnosis Notes',help='This field is used to take diagnosis notes')
    checkup_date = fields.Date(string='Checkup Date',help='This field is used to take patient checkup date')
    description = fields.Char('Description',help='This field is used to take description')
    medical_history = fields.Text(string='Medical History',help='This field is used to store patient medical history')
    website=fields.Char('Enter your url')
    sign_in = fields.Float('Sign In')
    password = fields.Char('Password',help='This field is used to take password')
    additional_information = fields.Char('Additional Information',help='This field is used to take additional information')


    priority = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Priority')
    blood_group = fields.Selection([
        ('A', 'A'),
        ('A+', 'A+'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('AB', 'AB'),
        ('O+', 'O'),
    ], string='Blood Group')
