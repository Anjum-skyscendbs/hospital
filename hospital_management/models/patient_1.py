from odoo import models, fields, api
from datetime import date


class Patient(models.Model):
    _name = 'hospital.patient'
    _rec_name = 'patient_name'
    _description = 'Hospital Patient'

    ### SIMPLE FIELDS
    # '<field_name>' = fields.<FIELD_CLASS>(<PARAMS>)
    # Here basically we are creating an object of one of the fields classes.

    patient_name = fields.Char(string='Patient Name', required=True, translate=True,
                               help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID', help='This field is used to take patient id')
    age = fields.Integer(string='Age', help='This field is used to take patient age')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    weight = fields.Float(string='Weight (kg)', help='This field is used to take patient weight', digits=(16, 3))
    height = fields.Float(string='Height (ft)', help='This field is used to take patient height', digits=(16, 3))

    # _order = '<field_name>' or '<field_name> desc'
    # This will be used to sort the fields with a field in either ascending or descending order
    # _order = 'sequence'
    sequence = fields.Integer('Sequence')

    # hospital_name = fields.Char(string="Hospital name",size=4)
    # print(hospital_name this field take a limited char size=4)

    email = fields.Char('Email', help='This field is used to take patient email')
    phone_number = fields.Char(string='Phone Number', size=10, help='This field is used to take patient phone number')
    address = fields.Char('Address', help='This field is used to take patient address')
    is_admitted = fields.Boolean(string='Admitted', help='This field is used to check that patient is admitted or not')

    birthdate = fields.Date('Birthdate', index=True, help='This field is used for birthdate of patient')
    notes = fields.Text('Notes', help='This field is used for notes')
    today = date.today()
    print("\n\n\ntoday:::::::::::>>>>>>>>>>>>>>>", today)

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    timestamp = fields.Date('Timestamp', readonly=True)
    Marital_status = fields.Selection([('married', 'Married'), ('unmarried', 'Unmarried'), ('single', 'Single')],
                                      string='Marital Status')

    checkup_date = fields.Date(string='Checkup Date', help='This field is used to take patient checkup date')
    medical_history = fields.Text(string='Medical History', help='This field is used to store patient medical history')
    url = fields.Char('URL')
    sign_in = fields.Float('Sign In')
    password = fields.Char('Password', help='This field is used to take password')
    additional_information = fields.Char('Additional Information',
                                         help='This field is used to take additional information')
    template = fields.Html('Template')
    total_price = fields.Float(string='Total Marks')

    priority = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Priority')
    blood_group = fields.Selection([
        ('A', 'A'),
        ('A+', 'A+'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('AB', 'AB'),
        ('O+', 'O'),
    ], string='Blood Group')

    state = fields.Selection([('admit', 'Admit'),
                              ('waiting','Waiting'),
                              ('recovery','Recovery'),
                              ('discharge', 'Discharge')], 'State', default='admit')

    # Created a function of Button in this file
    # function name is action_test sel

    def action_test(self):
        print("Button Clicked !!!!!")

    # Following are the Relational Fields will be used to connect with other models.
    # relational fields will be used to connect with other models.
    # you can create different relations with models such as Many2one, One2many and Many2many.
    # The first attribute for any relational field will be a comodel_name.
    # This comodel is the name of another model with which you're trying to create a relationship.

    # This is also a Relational field of Using Many2one in diseases model.

    diseases_id = fields.Many2one('hospital.diseases', 'Diseases')

    # 1) this is the required field type one Many2one in the department model.

    department_id = fields.Many2one('hospital.department', 'Department')

    # 2) The One2many field will have the first attribute as the comodel name being a relational field.

    # The second attribute is the inverse field which has to be the name of the field in the comodel.
    # This field will be a many2one field for current model (hospital) in comodel (appointment).
    # We will add _ids suffix to the One2many field.
    # The third attribute is the label fo the field.
    # This field is not stored in the database table.

    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', limit=2)

    # This is one2many field of Medicines which is define in inverse field of medicines_id
    # It is used to show this field in the On the Other Side of the model

    medicines_ids = fields.One2many('hospital.prescription', 'patient_id', 'Prescription')

    # 3) this is uses many2many field for the facility

    # The Many2many field will have the first attribute as the comodel_name being a relational field.
    # The second attribute is the label of the field.
    # The field does not get stored in the table in database.
    # Unlike O2M it does not have an inverse field.
    # Here it creates a lookup table with the name "'comodel's table name + _ + current model's table name + '_'  + rel".
    # So in our case it will be hospital_facility_hospital_patient_rel

    facility_ids = fields.Many2many('hospital.facility', 'pat_fact_rel', 'patient_id', 'fact_id', 'Facilities', limit=2)

    ref = fields.Reference([('hospital.patient', 'Patient'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')

    parent_id = fields.Many2one('hospital.patient', 'Monitor')
    # This is a reserved field used for hierarchy.
    # It is basically a many2one field to itself.

    child_ids = fields.One2many('hospital.patient', 'parent_id', 'Subordinates')
    # This is also a reserved field and works for hierarchy.
    # It is an O2M field and  field will be always parent_id

    # prescription_ids=fields.One2many('hospital.prescription','prescription_ids')

    # This One2Many field will have the first attribute as the comodel name being a relational field.
    # This field will be many2one field for current model(hospital) in comdel (appointment).
    # we will add _ids suffix to the one2many field.
    # The Third attribute is the label for the field.
    # This field is not stored in the database table.

    # 4) this sub_total is for calculate the sub total in the main page in the Notebook session
    # this is used to calculate a total price of medicine according to the Quantity
    # method name is calc_sub_total.
    # For Computing the total price of the medicine.

    sub_total = fields.Float(compute='_calc_sub_total', string='Total Amount')
    @api.depends('medicines_ids')
    def _calc_sub_total(self):
        """
     This method calculates the total price based on quantity and medicine price.
    """
        for record in self:
            total = 0.0
            for medicines in record.medicines_ids:
                total += medicines.sub_total
            record.sub_total = total

        # 1) In below case it will return records which have active set.
        # This will show in the Terminal that records are in active stage or not

        active_records = self.filtered('active')
        print("ACTIVE RECORDS", active_records)

        # 2) The second way is to using lambda function where you can use proper conditions to filter records.
        # Another way of filtering the data in the module using lambda function in it.

        female_records = active_records.filtered(lambda r: r.gender == 'female')
        male_records = active_records.filtered(lambda r: r.gender == 'male')
        print("FEMALE RECORDS", female_records)
        print("MALE RECORDS", male_records)
