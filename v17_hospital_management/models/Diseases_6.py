from odoo import models,fields

class Diseases(models.Model):
    _name='hospital.diseases'
    _description='diseases'

    _rec_name='diseases_name'

    diseases_name=fields.Char(string='Diseases')
    code = fields.Char('Code', size=5)




