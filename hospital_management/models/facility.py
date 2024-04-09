from odoo import models,fields

class Facility(models.Model):
    _name='hospital.facility'
    _description='facility'


patient_name = fields.Char(string='Patient Name', required=True,help='This field is used to take patient name')
patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')
word_rooms=fields.Selection(selection=[('operating room',' Operating Room'),
                                                   ('patient room',' Patient Room'),
                                                   ('icu room',' ICU Room'),
                                                   ('radiology room',' Radiology Room')])

phone_number = fields.Char(string='Phone Number', size=10, help='This field is used to take patient phone number')


# The mapping will help us fetch the activities to be displayed against the student.
facility = fields.Many2many('hospital.facility','pat_act_rel','patient_id','facility', limit=2)
 # You can also write the many2many field along with the details of lookup table.
# Firstly you need to give the name of the model as first attribute.


facility = fields.Many2many('hospital.facility', 'pat_act_rel', 'patient_id', 'act_id', 'Activities', limit=2)

