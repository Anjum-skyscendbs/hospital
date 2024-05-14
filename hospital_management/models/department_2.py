from odoo import models,fields

class Department(models.Model):
    _name='hospital.department'
    _description='department'

    _rec_name='patient_name'

    # department_id=fields.Selection(selection=[('gynecology','Gynecology'),
    #                                                ('physiotherapy','Physiotherapy'),
    #                                                ('odonotology','odonotology'),
    #                                                ('nursing','Nursing'),
    #                                                ('medicines','Medicines'),
    #                                                ('physician','Physician'),])

    patient_name=fields.Char(string='Patient Name', required=True,)
    age = fields.Integer(string='Age',help='This field is used to take patient age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    is_admitted = fields.Boolean(string='Admitted', help='This field is used to check that patient is admitted or not')
    department=fields.Char(string='Department name')
