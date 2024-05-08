from odoo import models, fields, api


class Medicines(models.Model):
    _name = 'hospital.medicines'
    _description = 'medicines'

    _rec_name = 'medicines_name'

    medicines_name = fields.Char('Medicines name')
    medicines_id = fields.Many2one('hospital.patient', string='Medicines')
    quantity = fields.Float(string='Quantity/Dose')
    sub_total = fields.Float(string='Sub Total')


