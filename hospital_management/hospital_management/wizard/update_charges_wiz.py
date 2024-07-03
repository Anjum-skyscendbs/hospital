from odoo import models,fields


class UpdatePatientWizard(models.TransientModel):
    _name = 'update.charges.wizard'
    _description = 'Update Patient Charges Wizard'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    charges = fields.Float('charges')

    def update_charges(self):

        pat_obj = self.env['hospital.patient']
        print("SELF CONTEXT,#########", self._context)
        print("ENV CONTEXT,#########", self.env.context)
        if self.patient_id.ids:
            patient = self.patient_id
        else:
            patient = pat_obj.browse(self._context.get('active_ids'))
        patient.write({'charges': self.charges})
