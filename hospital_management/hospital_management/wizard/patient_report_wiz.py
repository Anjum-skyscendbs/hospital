from odoo import models, fields

class PatientReportWizard(models.TransientModel):
    _name = 'patient.report.wiz'

    diseases_id = fields.Many2one('hospital.diseases','Diseases')

    def print_report(self):
        """
        This method is used to print the report for diseases's of a Patient
        ----------------------------------------------------
        @param self:object pointer
        """
        patient_obj = self.env['hospital.patient']
        patient = patient_obj.search([('diseases_id','=',self.diseases_id.id)])
        data = {}
        data['form'] = self.read()[0]
        if not patient:
            #TODO: Raise a Validation Error
            pass
        return self.env.ref('hospital_management.action_report_patient').report_action(patient, data=data)




