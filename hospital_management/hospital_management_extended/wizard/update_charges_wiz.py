from odoo import models, fields

class UpdatePatientWizard(models.TransientModel):
    _inherit = 'update.charges.wizard'

    height = fields.Float('Height')
    weight = fields.Float('Weight')

    def update_charges(self):


        # It creates a new Odoo recordset object named  (pat_obj )
        # It uses the Environment (self.env) to access the hospital.patient model.
        # It is calls a parent method named update_charges.
        # The Write Method allows you to Update specific fields in an existing Odoo Records.
        # The self.patient_id part likely refers to a field within the class that holds a Many2one relationship with the hospital.patient model.
        # The .ids attribute accesses the list of IDs associated with the Many2one field.
        # It uses the browse method to fetch a recordset based on the IDs stored in the active_ids key within
        # the Odoo context (self._context).
        # The active_ids context key typically holds the IDs of the currently selected records in the Odoo interface.
        # In this case, it's assumed that you're trying to update the weight and height of the currently

        pat_obj = self.env['hospital.patient']
        super().update_charges()
        if self.patient_id.ids:
            patient = self.patient_id
        else:
            patient = pat_obj.browse(self._context.get('active_ids'))
        patient.write({
            'height': self.height,
            'weight': self.weight
        })