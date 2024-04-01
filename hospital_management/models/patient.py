from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    patient_name = fields.Char(string='Name', required=True, translate=True)  # Changed field name to follow Python naming conventions
    age = fields.Integer(string='Age')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    weight = fields.Float(string='Weight (kg)')
    height = fields.Float(string='Height')

    email = fields.Char('Email')
    phone_number = fields.Char(string='Phone Number',size=10)
    address = fields.Char('Address')
    is_admitted = fields.Boolean(string='Admitted')
    birthdate = fields.Date('Birthdate')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    timestamp = fields.Date('Timestamp', readonly=True)
    Marital_status = fields.Selection([('married', 'Married'), ('unmarried', 'Unmarried'), ('single', 'Single')], string='Marital Status')

    notes = fields.Text('Notes')
    diagnosis_notes = fields.Html(string='Diagnosis Notes')
    last_checkup_date = fields.Date(string='Last Checkup Date')
    description = fields.Char('Description')
    medical_history = fields.Text(string='Medical History')
    sign_in = fields.Float('Sign In')
    priority = fields.Selection([(str(ele), str(ele)) for ele in range(6)], 'Priority')
