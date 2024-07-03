from odoo import models, fields, api, _

class Appointment(models.Model):
    _name='hospital.appointment'
    _description='Appointment'

    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Patient Name', required=True, translate=True,help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID',help='This field is used to take patient id')
    age = fields.Integer(string='Age', help='This field is used to take patient age')
    # seq_num=fields.Char(string='Seq no.', readonly=True, copy=False,index=True, default= lambda self:_('New'))



    email = fields.Char('Email', help='This field is used to take patient email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    # photo=fields.Image("Image")

    # Diseases=fields.Selection(selection=[('fever','Fever'),
    #                                      ('diabetes','Diabetes'),
    #                                      ('cholera','Cholera'),
    #                                      ('high blood pressure','High Blood Pressure'),
    #                                      ('headaches','Headaches')],help='This field show the list of diseases')


    # Exercise-2 Q-11 Add an amount field which shows the currency in Canadian Dollar.
    currency_id = fields.Many2one('res.currency', 'Currency')
    charges = fields.Monetary(currency_field='currency_id',string='Charges')

    sequence=fields.Integer(string="Sequence")

    phone_number = fields.Char(string='Phone Number', size=10,help='This field is used to take patient phone number')
    address = fields.Char('Address',help='This field is used to take patient address')

    checkup_date = fields.Date(string='Checkup Date',help='This field is used to take patient checkup date')

    # Exercise-2 Q-15. Add a field where you can add a file and make it such that the file content is stored in the database.
    document = fields.Binary('Document')
    # Binary field is used to store the binary data basically content of a document


    # Exercise-2 Q-13 Add a field where you can add a file. Preserve the file name.
    file_name = fields.Char('File Name')

    # Exercise-2 Q-14 Add a field where you can add an image
    photo = fields.Image('Photo')
    # In Image field you can upload an image.

    # appointment_id = fields.Many2one('hospital.appointment')


    # Exercise-4 Q-15,16.Add an onchange method for multiple fields to update another field’s value.

    @api.onchange('gender')
    def onchange_gender(self):
        """
        Onchange method to set default Charges for male and female
        ------------------------------------------------------
        """
        for patient in self:
            # charges = 0.0
            if patient.gender == 'female':
                charges = 500.0
            elif patient.gender == 'male':
                charges = 1000.0
            else:
                charges = 0.0
            patient.charges = charges
            print("___________Patient Charges")


