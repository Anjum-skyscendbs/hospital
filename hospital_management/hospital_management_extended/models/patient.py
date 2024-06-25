from odoo import models, fields, api


class Patient(models.Model):
    # If you use only _inherit it will add / modify in to existing
    _inherit = 'hospital.patient'

    height = fields.Float('Height(cm)')
    weight = fields.Float('Weight(kg)')
    extra_notes = fields.Html('Extra Notes')


    def print_patient(self):
        super().print_patient()
        print(" **************************** NEW METHOD")


