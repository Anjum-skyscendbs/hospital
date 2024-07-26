from odoo import models, fields, api
class PatientAnalysis(models.Model):
    _name = 'patient.analysis'
    _description = 'Patient Analaysis'
    _auto = False #not to create a model for this table.

    patient_name = fields.Char('Patient Name', translate=True)
    age = fields.Integer('Age')
    department_id = fields.Many2one('hospital.department', 'Department')

    # diseases_id = fields.Many2one('hospital.diseases', 'Diseases')

    medicines_id = fields.Many2one('hospital.medicines', 'Medicines')

    gst = fields.Float('GST')
    sgst = fields.Float('SGST')
    other_tax = fields.Float(string='TOTAL TAX')
    # tax_perc = fields.Integer(string='Tax Percentage(%)')


    @api.model
    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW patient_analysis_view AS (
                SELECT hp.id,
                    pt.patient_name,
                    pt.age,
                    pt.department_id,
                    hp.medicines_id,
                    hp.gst,
                    hp.sgst,
                    hp.other_tax
                    FROM 
                    hospital_patient pt,
                    hospital_prescription hp
                WHERE
                    pt.id = hp.patient_id)
        """)
