from odoo import models,fields,api


class Department(models.Model):

    _inherit = ['mail.thread','mail.activity.mixin','hospital.department']
    _name = 'hospital.department'

    color = fields.Integer('Color')

    #Exercise-6 Q-16 Make a tracking of the records such that whenever a field is modified you will
    # have the track of it in your chatter.
    contact_number = fields.Char(string='Contact Number',tracking=True,size=10)



