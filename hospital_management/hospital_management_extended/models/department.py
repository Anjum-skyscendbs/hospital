from odoo import models,fields,api


class Department(models.Model):

    _inherit = ['mail.thread','mail.activity.mixin','hospital.department']
    _name = 'hospital.department'

    color = fields.Integer('Color')


