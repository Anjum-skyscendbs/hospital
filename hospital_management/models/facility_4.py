from odoo import models, fields


class Facility(models.Model):
    _name = 'hospital.facility'
    _description = 'facility'
    _rec_name = 'word_rooms'

    patient_name = fields.Char(string='Patient Name', required=True, help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID', help='This field is used to take patient id')
    word_rooms = fields.Selection(selection=[('operating room', 'operating Room'),
                                             ('patient room', 'patient Room'),
                                             ('Icu room', 'ICU Room'),
                                             ('radiology room', 'Radiology Room')])

    phone_number = fields.Char(string='Phone Number', size=10, help='This field is used to take patient phone number')
