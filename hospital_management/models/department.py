from odoo import models,fields

class Department(models.Model):
    _name='hospital.department'
    _description='department'

    # ref = fields.Reference([('hospital.patient', 'patient'),
    #                         ('res.users', 'Users'),
    #                         ('res.partner', 'Contacts')], 'Reference')

    department=fields.Selection(selection=[('gynecology','Gynecology'),
                                                   ('physiotherapy','Physiotherapy'),
                                                   ('odonotology','odonotology'),
                                                   ('nursing','Nursing'),
                                                   ('medicines','Medicines'),
                                                   ('physician','Physician'),])

    patient_name=fields.Char(string='Patient Name', required=True,)
    age = fields.Integer(string='Age',help='This field is used to take patient age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    # birthdate = fields.Date('Birthdate', index=True,help='This field is used for birthdate of patient')
    # Marital_status = fields.Selection([('married', 'Married'), ('unmarried', 'Unmarried'), ('single', 'Single')],
    #                               string='Marital Status')
    is_admitted = fields.Boolean(string='Admitted', help='This field is used to check that patient is admitted or not')


    # Relational Fields
    # relational fields will be used to connect with other models.
    # you can create different relations with models such as Many2one, One2many and Many2many.
    # The first attribute for any relational field will be a comodel_name.
    # This comodel is the name of another model with which you're trying to create a relationship.

    # department = fields.Many2one('hospital.department', 'Department', ondelete='restrict')
