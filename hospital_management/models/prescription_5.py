from odoo import fields,models
class Prescription(models.Model):
    _name='hospital.prescription'
    _description='Prescription'
    _rec_name = 'disease'


    patient_name=fields.Char(string='Patient Name',required=True, help='This field is used to take patient name')
    # prescription_ids = fields.Many2one('hospital.prescription','Prescription')

    # patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')

    disease=fields.Selection(selection=[('high blood pressure','High Blood Pressure'),
                                        ('diabetes','Diabetes'),
                                        ('cholera','Cholera'),
                                        ('fever','Fever'),
                                        ('headaches','Headaches')])


