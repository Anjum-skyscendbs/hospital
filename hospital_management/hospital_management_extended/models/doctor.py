from odoo import models, fields, api


class Doctor(models.Model):
    _inherit = 'hospital.diseases'
    _name = 'hospital.doctor'

    # department_id = fields.Many2one('hospital.department', 'Department')
    doctor_name = fields.Char(string='Doctor Name')

    qualification = fields.Char('Qualification')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    disease_ids = fields.Many2many('hospital.diseases', 'patient_dise_rel', 'patient_id', 'disease', 'Diseases')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    currency_id = fields.Many2one('res.currency', 'Currency')
    charges = fields.Monetary(currency_field='currency_id', string='Charges')



