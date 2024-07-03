from odoo import models,fields

class Department(models.Model):
    _name='hospital.department'
    _description='department'

    _rec_name='department'


    # department_id=fields.Selection(selection=[('gynecology','Gynecology'),
    #                                                ('physiotherapy','Physiotherapy'),
    #                                                ('odonotology','odonotology'),
    #                                                ('nursing','Nursing'),
    #                                                ('medicines','Medicines'),
    #                                                ('physician','Physician'),])
    # department_id = fields.Many2one(string='Department',
    #                                 help='Department of the doctor')
                                    # related='doctor_id.department_id')

    # doctor_id = fields.Many2one('hospital.doctor', string="Doctor",
    #                             help='Name of the doctor')
    #                             domain=[('job_id.name', '=', 'Doctor')])

    is_doctor = fields.Boolean(string='Is Doctor', help='True for doctors')

    # patient_name=fields.Char(string='Patient Name', required=True,)
    age = fields.Integer(string='Age',help='This field is used to take patient age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    department=fields.Char(string='Department')

