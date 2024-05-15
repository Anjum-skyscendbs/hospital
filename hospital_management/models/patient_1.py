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
    _order = 'sequence'

    # Exercise-2 Q-24 Add a sequence field and add a functionality such that you can drag and drop
    # records to change the sequence.
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


    # Exercise-2 Q-23. Add a state field on your main model and add atleast 5 states. Assign a default state.
    # Display the states on progressbar on form view
    state = fields.Selection([('admit', 'Admit'),
                              ('waiting', 'Waiting'),
                              ('recovery', 'Recovery'),
                              ('discharge', 'Discharge'),
                              ('draft', 'Draft'),
                              ('left', 'Left'),
                              ], 'State', default='admit')

    # Following are the Relational Fields will be used to connect with other models.
    # relational fields will be used to connect with other models.
    # you can create different relations with models such as Many2one, One2many and Many2many.
    # The first attribute for any relational field will be a comodel_name.
    # This comodel is the name of another model with which you're trying to create a relationship.

    # This is also a Relational field of Using Many2one in diseases model.

    # Exercise-3 Q-1,Q-6 Having 'it' in substring in their name to select it’ as a substring in their name
    # should be allowed to select.

    diseases_id = fields.Many2one('hospital.diseases', 'Diseases')
    # Solution : domain="[('diseases_name','ilike','it')]"

    # 1) this is the required field type one Many2one in the department model.

    # Exercise-2 Q-6 If a record is selected in a many2one field, it should not be possible to delete the
    # record from the model of many2one.
    department_id = fields.Many2one('hospital.department', 'Department', ondelete='restrict')

    # 2) The One2many field will have the first attribute as the comodel name being a relational field.

    # The second attribute is the inverse field which has to be the name of the field in the comodel.
    # This field will be a many2one field for current model (hospital) in comodel (appointment).
    # We will add _ids suffix to the One2many field.
    # The third attribute is the label fo the field.
    # This field is not stored in the database table.

    # Exercise-2 Q-5,Q-7 Create a functionality such that whenever I delete a main record all the records in
    # its one2many should be deleted.

    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', limit=2)

    # This is one2many field of Medicines which is define in inverse field of medicines_id
    # It is used to show this field in the On the Other Side of the model.

    medicines_ids = fields.One2many('hospital.prescription', 'patient_id', 'Prescription')

    # 3) this is uses many2many field for the facility

    # The Many2many field will have the first attribute as the comodel_name being a relational field.
    # The second attribute is the label of the field.
    # The field does not get stored in the table in database.
    # Unlike O2M it does not have an inverse field.
    # Here it creates a lookup table with the name "'comodel's table name + _ + current model's table name + '_'  + rel".
    # So in our case it will be hospital_facility_hospital_patient_rel

    # Exercise-2 Q-4,Q-8 Give the table user defined name. Also give user defined name for the columns in this table
    facility_ids = fields.Many2many('hospital.facility', 'patient_fact_rel', 'patient_id', 'fact_id', 'Facilities')

    # Exercise-2 Q-12 Add a reference field where you can select a record from multiple models.
    ref = fields.Reference([('hospital.patient', 'Patient'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')

    # Reference field is a combination of Selection and M2O fields.
    # The first parameter will be same as selection a list of tuple.
    # So here the (first element) key must be a model name and the (second element) value can be anything.
    # On the screen it displays a static dropdown similar to selection where you can select one fo the models.
    # As soon as you select the model it shows another field where you can select a record related to the selected model.
    # This will be a varchar field in the database.
    # It stores the modelname + ',' + id of the selected record.

    # Exercise-2 Q-26. Add a hierarchy in the model of your many2one field. Use another field other
    # than parent_id for this hierarchy
    parent_id = fields.Many2one('hospital.patient', 'Monitor')
    # This is a reserved field used for hierarchy.
    # It is basically a many2one field to itself.

    child_ids = fields.One2many('hospital.patient', 'parent_id', 'Subordinates')

    # This is also a reserved field and works for hierarchy.
    # It is an O2M field and  field will be always parent_id

    # Exercise-2 Q-25 Add a hierarchy on your main model. The hierarchy should be stored in the character field.
    parent_path = fields.Char('Parent Path', index=True)

    # This is a reserved field which is used only if we have hierarchy in the model.
    # It will be used for faster searching of the extended hierarchy. (Subordinates of subordinates)
    # Not needed on the view.
    # It stores the complete hierarchy of all the parent's ids including current record's id.

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

    # total price of medicines,write a compute method to calculate its value and fields in it.
    # In the above I created a function name api.depends in it.
    # To calculate this medicines calc total price is function is used for this.
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

        # # < is used to check subset
        print("SUBSET", female_records < active_records)
        # # <= is used to check either subset or same set
        print("SUB OR SAME1", male_records <= active_records)
        print("SUB OR SAME2", active_records <= active_records)

        # > is used to check superset
        print("SUPER", active_records > female_records)
        # # >= is used to check superset or same set
        print("SUPER OR SAME 1", active_records >= male_records)
        print("SUPER OR SAME 2", active_records >= active_records)
        #
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

        # # TODO: Future development
        #
        # print("PRINT")
        # print("SELFFFFFF", self)
        # print("ENVIRONMENT", self.env)
        # print("ENVIRONEMTN  ATTRS", dir(self.env))
        # print("ARGS", self.env.args)
        # print("CURSOR", self.env.cr)
        # print("UID", self.env.uid)
        # print("USER", self.env.user)
        # print("CONTEXT", self.env.context)
        # print("COMPANY", self.env.company)
        # print("COMPANIES", self.env.companies)
        # print("LANG", self.env.lang)
        #
        # appt_obj = self.env['hospital.appointment']
        # print("APPT OBJ", appt_obj)
        # depa_obj = self.env['hospital.department']
        # print("DEP OBJ", depa_obj)
        #
        # form_view_pat = self.env.ref('hospital.view_patient_form')
        # print("FORM VIEW PAT", form_view_pat)

    def create_rec(self):
        """
        This is a button method which is used to demonstrate create() method.
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        vals1 = {
            'patient_name': 'kajal',
            'patient_id': 21,
            'gender': 'female',
            'blood_group': 'A+',
            'active': True,
            'age': 34,
            'birthdate': '1989-04-01',

        }
        vals2 = {
            'patient_name': 'Hardik',
            'patient_id': 20,
            'gender': 'male',
            'blood_group': 'A',
            'active': True,
            'age': 19,
            'birthdate': '2004-05-17',


        }
        vals_lst = [vals1, vals2]
        # # Creating a new records in the same object
        new_pat = self.create(vals_lst)
        print("pat", new_pat)

    def update_rec(self):
        """
        Button's method to demonstrate write() method
        """
        # 0 is for creation
        # 1 is for updation
        # (1,<id>,{}) will update existing recrod in o2m.
        # 2 is for deletion
        # (2,<id>) will remove the record from o2m field and will be removed from the table.
        # 3 is for unlink
        # (3,<id>) will remove the record from o2m field but will keep in the table.
        # 4 is to link
        # 5 is used to unlink all records
        # (5,0,0) is used to unlink all records and keeps in the table.
        # 6 is used to link multiple records but overwrites existing ones
        # 6 first performs the 5 operation to remove existing records.
        # then uses 4 operation to link the new records
        vals = {
            'age': 29.0,
            'department_id': 4,
            'appointment_ids': [
                #  (5,0,0)
                #  (6,0,[1,2,3])
                #  (6,0,[8,19])
                (4, 1), (4, 2), (4, 3)
            ]
        }
        res = self.write(vals)
        print("RES", res)


        # In this Method using Browse Method.It uses id , list of ids to give records according to the ids
        # Another Way to using a browse Method
        # search_var = self.env['hospital.patient'].browse([12, 9])
        # for rec in search_var:
        #     print("Search Var........................", rec, "Name", rec.patient_name, "age", rec.age, 'gender',
        #           rec.gender)

        def browse_rec(self):

            pat_rec = self.browse(23)
            print("\nSTU REC--------------------------", pat_rec)
            pat_dict = pat_rec.read(
                ['name', 'age', 'patient_id', 'appoinment_ids', 'activity_ids'], load='')

            print("PATIENT DICCT----------------------", pat_dict)
            # M2O will give a tuple containing id and name (if load =='_classic_read')
            # M2O will give you id (if load != '_classic_read')

            print("DEPARTMENT", pat_dict[0]['department_id'])
            # O2M  will give a list of ids
            print("Appointment", pat_dict[0]['appointment_ids'])
            # M2M will give a list of ids
            print("ACT", pat_dict[0]['activity_ids'])
            patient = self.browse([1, 2])
            print("\nPatients--------------------------", patient)


    def copy_rec(self):
            default = {
                'patient_name': self.patient_name + ' (copy)',
                'email': False
            }
            new_rec = self.copy(default=default)
            print("\nNEW REC", new_rec)

    def delete_rec(self):
            res = self.unlink()
            print("RES", res)

    def search_rec(self):
            all_patient = self.search([])
            # When you pass a blank domain it will return all the records.
            print("ALL PATIENTS", all_patient)

            # When you pass a condition in domain it will pass only matching records
            male_patient = self.search([('gender', '=', 'male')])
            print("MALE PATIENTS", male_patient)

            # When you pass offset it will skip no of records from the result
            offset_3_patient = self.search([], offset=3)
            print("SKIP 3 RECORDS", offset_3_patient)

            # When you pass limit it will limit the max no of records to fetch
            limit_4_patient = self.search([], limit=4)
            print("First 4 RECORDS", limit_4_patient)

            # When you pass offset and limit both the priority will be offset and then limit
            off_2_limit_4_patient = self.search([], offset=2, limit=4)
            print("SKIP 2 MAX 4 RECORDS", off_2_limit_4_patient)

            # When you pass order you can sort the records by a specific field
            sort_asc_patient_name = self.search([], order='patient_name')
            print("SHORT BY NAME<", sort_asc_patient_name)

            # When you pass desc after the field it will sort in descending order
            sort_desc_patient_name = self.search([], order='patient_name desc')
            print("SHORT BY NAME< DESC", sort_desc_patient_name)

            # When you pass offset, limit and order the priority goes to order then offset and then limit
            sort_asc_patient_name = self.search([], offset=2, limit=4, order='patient_name')
            print("SHORT BY NAME< OFFSET LIMIT", sort_asc_patient_name)

            # When you pass count=True it returns no of records rather than a recordset
            no_of_patient = self.search([], count=True)
            print("TOTAL PATIENT", no_of_patient)
            no_of_female_patient_name = self.search([('gender', '=', 'female')], count=True)
            print("FEMALE PATIENT", no_of_female_patient_name)

            ## search_count
            no_of_patient = self.search_count([])
            print("TOTAL PATIENT", no_of_patient)
            no_of_female_patient_name = self.search_count([('gender', '=', 'female')])
            print("FEMALE PATIENT", no_of_female_patient_name)

            ### search_read
            patient_name_lst = self.search_read(fields=['patient_name', 'age', 'department_id', 'appointment_ids', 'facility_ids'])
            print("SEARCH READ Patient", patient_name_lst)
            patient_name_lst_2 = self.search_read(
                fields=['patient_name', 'age', 'department_id', 'appointment_ids', 'facility_ids'],
                offset=2,
                order='patient_name')
            print("SEARCH READ PATIENT", patient_name_lst_2)
