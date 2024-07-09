from odoo import models, fields, api
class PatientAnalysis(models.Model):
    _name = 'patient.analysis'
    _auto = False

    patient_name = fields.Char('Patient Name', translate=True)
    age = fields.Integer('Age')
    medicines_id = fields.Many2one('hospital.medicines', 'Medicines')
    gst = fields.Float('GST')
    sgst = fields.Float('SGST')
    total_tax = fields.Float(string='TOTAL TAX')
    # tax_perc = fields.Integer(string='Tax Percentage(%)')


    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW patient_analysis_view AS (
                SELECT 
                    hp.gst,
                    hp.sgst,
                    hp.id AS id,
                    pt.age,
                    hp.medicines_id,
                    pt.patient_name
                    FROM 
                    hospital_patient pt,
                    hospital_prescription hp
                WHERE
                    pt.id = hp.patient_id
            )
        """)
