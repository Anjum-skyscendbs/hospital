from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    checkup_date = fields.Date(string='Checkup Date', help='This field is used to take patient checkup date')
    sign_in = fields.Float('Sign In')
