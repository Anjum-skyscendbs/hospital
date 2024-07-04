from odoo import api, fields, models

class Employee(models.Model):
    _inherit = 'hr.employee'

    #Exercise-6 Q-13
    aadhaar_no = fields.Char('Aadhaar Card No')
    pan_card_no = fields.Char('Pan Card Number')