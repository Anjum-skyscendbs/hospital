from odoo import fields,models

class Appointment(models.Model):
    _name='hospital.appointment'
    _description='Appointment'


    patient_name = fields.Char(string='Patient Name', required=True, translate=True,help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')

    Charges = fields.Monetary(currency_field='currency_id',string='Charges')
    currency_id = fields.Many2one('res.currency', 'Currency')

    phone_number = fields.Char(string='Phone Number', size=10,help='This field is used to take patient phone number')
    address = fields.Char('Address',help='This field is used to take patient address')

    is_admitted = fields.Boolean(string='Admitted',help='This field is used to check that patient is admitted or not')
    checkup_date = fields.Date(string='Checkup Date',help='This field is used to take patient checkup date')

    document = fields.Binary('Document')
    photo = fields.Image('Photo')


    # appointment = fields.One2many('hospital.appointment',limit=2)
    # The One2many field will have the first attribute as the comodel name being a relational field.
    # The second attribute is the inverse field which has to be the name of the field in the comodel.
    # This field will be a many2one field for current model (student) in comodel (exam).
    # We will add _ids suffix to the One2many field.
    # The third attribute is the label fo the field.
    # This field is not stored in the database table.













from odoo import fields,models


class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subjects'

    _rec_name = 'sub_name'

    sub_name = fields.Char('Name')
    code = fields.Char('Code')


class SchoolExam(models.Model):
    _name ='school.exam'
    _description = 'Exam'

    subject_id = fields.Many2one('school.subject', 'Subject')
    total_marks = fields.Float('Total Marks')
    min_marks = fields.Float('Minimum Marks')
    obt_marks = fields.Float('Obtained Marks')
    student_id = fields.Many2one('school.student', 'Student', ondelete='cascade')
    # student_id is the inverse field for O2M field exam_ids in student
    # ondelete='cascade' will delete all (current model)exam records if (comodel) student record is deleted.

