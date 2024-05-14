from odoo import fields, models, api


class Prescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Prescription'
    _rec_name = 'medicines_id'

    # patient_name=fields.Char(string='Patient Name',required=True, help='This field is used to take patient name')
    #
    # patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')
    #
    # disease=fields.Selection(selection=[('high blood pressure','High Blood Pressure'),
    #                                     ('diabetes','Diabetes'),
    #                                     ('cholera','Cholera'),
    #                                     ('fever','Fever'),
    #                                     ('headaches','Headaches')])

    medicines_id = fields.Many2one('hospital.medicines', 'Medicines')
    quantity = fields.Integer("Quantity/Dose")
    patient_id = fields.Many2one('hospital.patient', 'Patient Name')
    total_price = fields.Float(compute="_calc_total_price", string='Total Price')

    # This is the Method of Medicines_id to fetch the data from Medicine Model and Multiply with the Quantity
    @api.depends('medicines_id', 'quantity')
    def _calc_total_price(self):
        a_total_price = 0
        for pr in self:
            a_total_price = pr.quantity * pr.medicines_id.total_price
            pr.total_price = a_total_price
