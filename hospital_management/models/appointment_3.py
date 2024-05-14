from odoo import models, fields, api

class Appointment(models.Model):
    _name='hospital.appointment'
    _description='Appointment'

    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Patient Name', required=True, translate=True,help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')
    age = fields.Integer(string='Age', help='This field is used to take patient age')

    email = fields.Char('Email', help='This field is used to take patient email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    # photo=fields.Image("Image")

    # Diseases=fields.Selection(selection=[('fever','Fever'),
    #                                      ('diabetes','Diabetes'),
    #                                      ('cholera','Cholera'),
    #                                      ('high blood pressure','High Blood Pressure'),
    #                                      ('headaches','Headaches')],help='This field show the list of diseases')

    charges = fields.Monetary(currency_field='currency_id',string='Charges')
    currency_id = fields.Many2one('res.currency', 'Currency')

    sequence=fields.Integer(string="Sequence")

    phone_number = fields.Char(string='Phone Number', size=10,help='This field is used to take patient phone number')
    address = fields.Char('Address',help='This field is used to take patient address')

    checkup_date = fields.Date(string='Checkup Date',help='This field is used to take patient checkup date')

    document = fields.Binary('Document')
    photo = fields.Image('Photo')

    appointment_ids = fields.Many2one('hospital.appointment', 'Appointment')




