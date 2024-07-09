from odoo import models, fields


class Facility(models.Model):
    _name = 'hospital.facility'
    _description = 'facility'
    _rec_name = 'wordrooms'

    patient_name = fields.Char(string='Patient Name', required=True, help='This field is used to take patient name')
    patient_id_no = fields.Integer(string='Patient ID', help='This field is used to take patient id')
    # wordrooms_id = fields.Selection(selection=[('operatings room', 'operatings Room'),
    #                                          ('patients room', 'patients Room'),
    #                                          ('Icu room', 'ICU Room'),
    #                                          ('radiology room', 'Radiology Room')])

    # phone_number = fields.Char(string='Phone Number', size=10, help='This field is used to take patient phone number')

    wordrooms = fields.Char(string='Wordrooms')
    room_no = fields.Integer('Room No')

    color = fields.Integer('Color')
