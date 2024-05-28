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

    # Exercise-2 Q-18 Add minimum 3 float ifelds in the one2many field’s model. These 3 fields are manually entered.
    gst = fields.Float(string='GST')
    sgst = fields.Float(string='SGST')
    other_tax = fields.Float(string='OTHER TAX')

    # Exercise-2 Q-19. Add two more float fields but the values of these two fields will be automatically
    # calculated from these 3 fields.The fields should not be stored in the database table.
    total_tax = fields.Float(string='TOTAL TAX', compute='_cal_total_tax')
    without_other_tax = fields.Float(string='TOTAL TAX (WITHOUT OTHER TAX)', compute='_cal_total_tax_without_other_tax')

    total_price = fields.Float(compute="_calc_total_price", string='Total Price')


    # Exercise-2 Q-20 Add another Integer field in the model of one2many which will calculate the
    # percentage from the above two fields.
    tax_perc = fields.Integer(string='Tax Percentage',compute='_calc_tax_perc')

    # This is the Method of Medicines_id to fetch the data from Medicine Model and Multiply with the Quantity
    # Total Price Calculate
    @api.depends('medicines_id', 'quantity')
    def _calc_total_price(self):
        a_total_price = 0
        for pr in self:
            a_total_price = pr.quantity * pr.medicines_id.total_price
            pr.total_price = a_total_price


    # This is the Method of Gst, Sgst, Other tax. It will calculate the total tax of 3 of all the tax.
    # total_tax = gst + sgst + other tax
    @api.depends('gst','sgst','other_tax')
    def _cal_total_tax(self):
        for prescription in self:
            prescription.total_tax = prescription.gst + prescription.sgst + prescription.other_tax


    # Exercise-2 Q-19 One of them should be total of this field and the other one should be additional of two fields
    # and subtraction of one field.The fields should not be stored in the database table.
    @api.depends('gst','sgst','other_tax')
    def _cal_total_tax_without_other_tax(self):
        for prescription in self:
            prescription.without_other_tax = (prescription.gst + prescription.sgst) - prescription.other_tax

    @api.depends('total_tax','without_other_tax')
    def _calc_tax_perc(self):
        for prescription in self:
            prescription.tax_perc = prescription.total_tax + prescription.without_other_tax

