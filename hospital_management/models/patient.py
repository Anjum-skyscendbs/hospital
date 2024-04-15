from odoo import models, fields
from datetime import date


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    ### SIMPLE FIELDS
    # '<field_name>' = fields.<FIELD_CLASS>(<PARAMS>)
    # Here basically we are creating an object of one of the fields classes.


    patient_name = fields.Char(string='Patient Name', required=True, translate=True,help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')
    age = fields.Integer(string='Age',help='This field is used to take patient age')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    weight = fields.Float(string='Weight (kg)',help='This field is used to take patient weight',digits=(16,3))
    height = fields.Float(string='Height (ft)',help='This field is used to take patient height',digits=(16,3))
    Diseases=fields.Selection(selection=[('high blood pressure','High Blood Pressure'),('diabetes','Diabetes'),('cholera','Cholera'),('heart attack','Heart Attack')],help='This field show the list of diseases')

    # _order = '<field_name>' or '<field_name> desc'
    # This will be used to sort the fields with a field in either ascending or descending order
    _order = 'sequence'
    sequence = fields.Integer('Sequence')

    hospital_name = fields.Char(string="Hospital name",size=4)
    # print(hospital_name this field take a limited char size=4)


    email = fields.Char('Email',help='This field is used to take patient email')
    phone_number = fields.Char(string='Phone Number', size=10,help='This field is used to take patient phone number')
    address = fields.Char('Address',help='This field is used to take patient address')
    is_admitted = fields.Boolean(string='Admitted',help='This field is used to check that patient is admitted or not')
    # print("is_admitted for the patient is admitted or not")


    birthdate = fields.Date('Birthdate', index=True,help='This field is used for birthdate of patient')
    notes = fields.Text('Notes',help='This field is used for notes')
    today = date.today()
    print(today)

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    timestamp = fields.Date('Timestamp', readonly=True)
    Marital_status = fields.Selection([('married', 'Married'), ('unmarried', 'Unmarried'), ('single', 'Single')], string='Marital Status')

    diagnosis_notes = fields.Text(string='Diagnosis Notes',help='This field is used to take diagnosis notes')
    checkup_date = fields.Date(string='Checkup Date',help='This field is used to take patient checkup date')
    description = fields.Char('Description',help='This field is used to take description')
    medical_history = fields.Text(string='Medical History',help='This field is used to store patient medical history')
    url = fields.Char('URL')
    sign_in = fields.Float('Sign In')
    password = fields.Char('Password',help='This field is used to take password')
    additional_information = fields.Char('Additional Information',help='This field is used to take additional information')
    # template = fields.Html('Template')

    priority = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Priority')
    blood_group = fields.Selection([
        ('A', 'A'),
        ('A+', 'A+'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('AB', 'AB'),
        ('O+', 'O'),
    ], string='Blood Group')


    # Button clicked to submit the form

    def action_test(self):
        print("Button Clicked !!!!!")

     # 1) this is the required field type one Many2One in the department

    department_id = fields.Many2one('hospital.department', 'Department')

    # 2) The One2many field will have the first attribute as the comodel name being a relational field.
    # The second attribute is the inverse field which has to be the name of the field in the comodel.
    # This field will be a many2one field for current model (student) in comodel (exam).
    # We will add _ids suffix to the One2many field.
    # The third attribute is the label fo the field.
    # This field is not stored in the database table.

    appointment_ids = fields.One2many('hospital.appointment','patient_id',limit=2)

    # 3) this field is uses many2many field for the facility

    facility_ids= fields.Many2many('hospital.facility', 'pat_fact_rel', 'patient_id', 'fact_id', 'Activities', limit=2)

    ref = fields.Reference([('hospital.patient', 'patient'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')


