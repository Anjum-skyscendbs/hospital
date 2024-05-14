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
    total_price = fields.Float(string='Total Price')

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
                              ('waiting', 'Waiting'),
                              ('recovery', 'Recovery'),
                              ('discharge', 'Discharge')], 'State', default='admit')

    # Following are the Relational Fields will be used to connect with other models.
    # relational fields will be used to connect with other models.
    # you can create different relations with models such as Many2one, One2many and Many2many.
    # The first attribute for any relational field will be a comodel_name.
    # This comodel is the name of another model with which you're trying to create a relationship.

    # This is also a Relational field of Using Many2one in diseases model.

    # Exercise-3 Q-1 Having 'it' in substring in their name to select it’ as a substring in their name
    # should be allowed to select.

    diseases_id = fields.Many2one('hospital.diseases', 'Diseases')
    # Solution : domain="[('diseases_name','ilike','it')]"

    # 1) this is the required field type one Many2one in the department model.

    # Exercise-2 Q-6 If a record is selected in a many2one field, it should not be possible to delete the
    # record from the model of many2one.
    department_id = fields.Many2one('hospital.department', 'Department', ondelete='restrict')

    # This is Many2one field which I am using in this wardrooms fields.
    # wordrooms_id = fields.Many2one('hospital.facility','Facility')

    # 2) The One2many field will have the first attribute as the comodel name being a relational field.

    # The second attribute is the inverse field which has to be the name of the field in the comodel.
    # This field will be a many2one field for current model (hospital) in comodel (appointment).
    # We will add _ids suffix to the One2many field.
    # The third attribute is the label fo the field.
    # This field is not stored in the database table.

    # Exercise-2 Q-5 Create a functionality such that whenever I delete a main record all the records in
    # its one2many should be deleted.

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

    # Exercise-2 Q-4,Q-8 Give the table user defined name. Also give user defined name for the
    # columns in this table
    facility_ids = fields.Many2many('hospital.facility', 'patient_fact_rel', 'patient_id', 'fact_id', 'Facilities')

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

    # Created a function of Button in this file
    # function name is action_test sel

    def action_test(self):
        print("Button Clicked !!!!!")

    # sub total of medicines,write a compute method to calculate its value and fields in it.
    # In the above I created a function name api.depends in it.
    # To calculate this medicines calc sub total is function is used for this.
    total_price = fields.Float(compute='_calc_total_price', string='Total Price')

    @api.depends('medicines_ids')
    def _calc_total_price(self):
        """
     This method calculates the total price based on quantity and medicine price.
    """
        for record in self:
            total = 0.0
            for medicines in record.medicines_ids:
                total += medicines.total_price
            record.total_price = total

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

        # Using a Mapping field and return the record in a list.
        # Mapped is used to map field values from records and return in a list.
        active_records_patient_name = active_records.mapped('patient_name')
        print("ACTIVE NAMES", active_records_patient_name)

        active_records_patient_name_age = active_records.mapped(lambda r: str(r.patient_name) + "," + str(r.age))
        print("ACITVE NAME AGE", active_records_patient_name_age)

        # sorted() is used to sort the records
        sort_by_age = active_records.sorted(key='age')
        print("SORT BY AGE", sort_by_age)

        sort_by_name = active_records.sorted(key='patient_name', reverse=True)
        print("SORT BY NAME", sort_by_name)

        # # RECORDSET OPERATIONS
        # # using in you can check whether a record exists in a recordset or not.
        # # works with a single record and not multiple records
        res = female_records in active_records
        print("RES", res)
        for fr in female_records:
            print("FR IN ACT", fr in active_records)

        res = female_records not in active_records
        print("RES", res)

        # < is used to check subset
        print("SUBSET", female_records < active_records)
        # <= is used to check either subset or same set
        print("SUB OR SAME1", male_records <= active_records)
        print("SUB OR SAME2", active_records <= active_records)

        # > is used to check superset
        print("SUPER", active_records > female_records)
        # >= is used to check superset or same set
        print("SUPER OR SAME 1", active_records >= male_records)
        print("SUPER OR SAME 2", active_records >= active_records)

        print("UNION", male_records | female_records)
        print("INTERSECTION", male_records & active_records)
        print("DIFF", active_records - female_records)

        for patient in self:
            # You can access the fields using '.'.
            # Normal field will directly give the value of the field
            print("NORMAL FIELD", patient.patient_name)
            # Relational fields will always give you a recordset.
            # M2O/Ref field will give you single record recordset
            # O2M/M2M will give you multiple records recordset.
            print("M2O FIELD", patient.department_id.patient_name)
            # IF there's a single record you can access the field with multiple '.' referecnes.
            print("O2M FIELD", patient.appointment_ids)
            # If there are multiple records you can not access the field directly.
            # print("Appointment FIELD",patient.appointment_ids # This will raise an error of singleton

            # You can use index in the recordset but if and only if there is a record
            if patient.appointment_ids:
                print("O@M APPOINTMENT PATIENT", patient.appointment_ids[0].patient_name)

            # # ensure_one() is used to validate a single record
            # patient.ensure_one() # NO ERROR
            # #patient.appointment_ids.ensure_one() # ERROR
            #
            # get_metadata() gives you the pre-defined fields / magic fields
            # It returns a dictionary containing id, create_date, create_uid, write_date, write_uid
            # mt_dt = patient.get_metadata()
            # print("MT DT", mt_dt)

        # In this Method using search in ORM to find the records according to the Condition
        # SEARCH METHOD

    def print_patient(self):
        search_var = self.env['hospital.patient'].search([('gender', '=', 'male')])
        print("Search Var........................", search_var)
        for rec in search_var:
            print("patient name.....................", rec.patient_name, 'gender......', rec.gender)

        # In this Method using search_count Method.It will count the total records in using search_count
        # search_var = self.env['hospital.patient'].search_count([('gender', '=', 'male')])
        # for rec in search_var:
        #     print("Search Var........................",search_var)

        # In this Method using Browse Method.It uses id , list of ids to give records according to the ids

        # search_var = self.env['hospital.patient'].browse([12,9])
        # for rec in search_var:
        #      print("Search Var........................",rec,"Name",rec.patient_name,"age",rec.age,'gender',rec.gender)

        # """
        #       This is a method of the button to demonstrate the usage of button
        #       -----------------------------------------------------------------
        #       @param self: object pointer / recordset
        #     """
        #   # TODO: Future development
        #
        #       print("PRINT")
        #       print("SELFFFFFF", self)
        #       print("ENVIRONMENT", self.env)
        #       print("ENVIRONEMTN  ATTRS", dir(self.env))
        #       print("ARGS", self.env.args)
        #       print("CURSOR", self.env.cr)
        #       print("UID", self.env.uid)
        #       print("USER", self.env.user)
        #       print("CONTEXT", self.env.context)
        #       print("COMPANY", self.env.company)
        #       print("COMPANIES", self.env.companies)
        #       print("LANG", self.env.lang)
        #
        #       appt_obj = self.env['hospital.appointment']
        #       print("APPT OBJ", appt_obj)
        #       depa_obj = self.env['hospital.department']
        #       print("DEP OBJ", depa_obj)
        #
        #       form_view_pat = self.env.ref('hospital.view_patient_form')
        #       print("FORM VIEW PAT", form_view_pat)

    def create_rec(self):
        #                 """
        #                 This is a button method which is used to demonstrate create() method.
        #                 ---------------------------------------------------------------------
        #                 @param self: object pointer
        #                 """
        vals1 = {
            'patient_name': 'Hirva',
            'active': True,
            'age': 34,
            'birthdate': '1989-04-01',
            'patient_id': 21,
            'gender': 'female',
            'blood_group': 'A+'
        }
        vals2 = {
            'patient_name': 'Nirav',
            'active': True,
            'age': 19,
            'birthdate': '2004-05-17',
            'patient_id': 20,
            'gender': 'male',
            'blood_group': 'A'

        }
        vals_lst = [vals1, vals2]
        # # Creating a new records in the same object
        new_pat = self.create(vals_lst)
        print("pat", new_pat)
