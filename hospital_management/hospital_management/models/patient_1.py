from odoo import models, fields, api, Command ,_
from datetime import date
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = 'hospital.patient'
    # _rec_name = 'sequence'
    _rec_name = 'patient_name'
    _description = 'Hospital Patient'

    patient_name = fields.Char(string='Patient Name', translate=True,
                               help='This field is used to take patient name')
    patient_id = fields.Integer(string='Patient ID', help='This field is used to take patient id')


    # Exercise-2 Q-17 Add an Integer field and add a functionality such that when you group the records
    # it shows the maximum of the values given in the field on the group in tree view.
    age = fields.Integer(string='Age',group_operator='max', help='This field is used to take patient age')
    # sum, min, max  default = sum
    # default attribute is used to provide default values to the field.
    # The value has to be specific to the field type

    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    # weight = fields.Float(string='Weight (kg)', help='This field is used to take patient weight', digits=(16, 3))
    # height = fields.Float(string='Height (ft)', help='This field is used to take patient height', digits=(16, 3))
    # # _order = '<field_name>' or '<field_name> desc'
    # This will be used to sort the fields with a field in either ascending or descending order
    _order = 'sequence'


    # _sql_constraints = []
    # This will be used to add constraints in SQL table.
    # It is a list of tuple where each tuple is one constraint
    # The tuple contains exactly 3 elements
    # First one is the name of the constraint
    # Second one is the constraint how we write in SQL
    # Third one is the warning that gets raised when constraint fail

    # Exercise-4 Q-19,20,21
    _sql_constraints = [
        ('check_age', 'check(age>=18)', 'The age has to be a at least 18!'),
        ('unique_patient_code', 'unique(patient_code)', 'The code of the patient must be unique!'),
        ('check_phone_number', 'check(LENGTH(phone_number) <= 10)', 'The Phone number must be 10 digit!!!'),
        ('unique_email_password', 'unique(email,password)', 'The Email-id and Password must be unique!!!')

    ]

    # Exercise-2 Q-24 Add a sequence field and add a functionality such that you can drag and drop
    # records to change the sequence.
    sequence = fields.Char('Sequence')

    reg_no =  fields.Char('Reg No',required=True, copy=False, default = lambda self:_('New'))

    patient_code = fields.Char('Patient Code', size=4)
    # size is used to limit the maximum no of characters to be stored.


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

    timestamp = fields.Datetime('Timestamp')
    timestamp_end = fields.Datetime("End Time")
    # readonly attribute will make the field to be non-editable


    checkup_date = fields.Date(string='Checkup Date', help='This field is used to take patient checkup date')
    medical_history = fields.Text(string='Medical History', help='This field is used to store patient medical history')
    url = fields.Char('URL')
    sign_in = fields.Float('Sign In')
    password = fields.Char('Password', help='This field is used to take password')

    # additional_information = fields.Char('Additional Information',
    #                                      help='This field is used to take additional information')
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

    # Exercise-3 Q-10 Add a boolean field and a text field. Put the text field in a separate page. Now
    # when the boolean field is checked then the page should be visible else it should be invisible.

    additional_information = fields.Text('Additional Information')
    summary = fields.Boolean('Summary')

    # Exercise-2 Q-23. Add a state field on your main model and add atleast 5 states. Assign a default state.
    # Display the states on progressbar on form view
    state = fields.Selection([('admit', 'Admit'),
                              ('waiting', 'Waiting'),
                              ('recovery', 'Recovery'),
                              ('discharge', 'Discharge'),
                              ('draft', 'Draft'),
                              ], 'State', default='admit')

    # Method of Changing the mode of Statubar while click on different buttons
    def action_confirm(self):
        self.state = 'waiting'
        # print("clicked on button")

    def action_done(self):
        self.state = 'recovery'

    def action_draft(self):
        self.state = 'discharge'

    def action_cancel(self):
        self.state = 'draft'

    # Exercise-3 Q-11 default = 'admit'

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

    # appointment_ids = fields.One2many('hospital.appointment', 'appointment_id', string="Appointment")
    # limit=2

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

    # Exercise-3 Q-2 In the many2many field only the records which are ending with ‘ts’ substring
    # should be allowed to select In the Facility field.
    # Solution :- domain = "[('wordrooms', '=like', '%ts')]"

    # Exercise-2 Q-12 Add a reference field where you can select a record from multiple models.
    ref = fields.Reference([('hospital.patient', 'Patient'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')

    photo = fields.Image('Photo')
    # In Image field you can upload an image.

    color = fields.Integer('Color')
    # This field is used for Color on Kanban

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
    # For e.g. 1/2/4/5/3
    # Here current record is with id 3, parent of 3 is 5, parent of 5 is 4, parent of 4 is 2 and finally parent of 2 is 1.

    company_id = fields.Many2one('res.company', 'Company')
    # This is the most important field in terms of reserved ones.
    # It represents the company of the records.
    # Company means the legal entity or Enterprise.
    # It becomes more important when we have multiple companies in one database.
    # It can be used to filter records as per the company.

    # function name is action_test sel

    # def action_test(self):
    #     print("Button Clicked !!!!!")

    # Exercise-2 Q-21 Now these two fields must be added in the database table. store=True
    total_tax = fields.Float(string='TOTAL TAX', compute='_cal_total_tax', store=True)

    # Exercise-2 Q-21 In the Main model where you have defined the one2many field add two float
    # fields which will get the total of all the records of one2many from the two
    # functional field which you have added.
    without_other_tax = fields.Float(string='TOTAL TAX (WITHOUT OTHER TAX)',
                                     compute='_cal_total_tax_without_other_tax', store=True)

    # 4) this sub_total is for calculate the sub total in the main page in the Notebook session
    # this is used to calculate a total price of medicine according to the Quantity
    # method name is calc_sub_total.
    # For Computing the total price of the medicine.
    # total price of medicines,write a compute method to calculate its value and fields in it.
    # In the above I created a function name api.depends in it.
    # To calculate this medicines calc total price is function is used for this.
    total_price = fields.Float(compute='_calc_total_price', string='TOTAL PRICE')

    @api.depends('medicines_ids')
    def _calc_total_price(self):
        """
         This method will calculate multiple fields.
        -------------------------------------------
        @param self : object pointer / recordset
        """
        print("SELF", self)
        # You can not access any fields from a recordset which contains multiple records
        # print("SELF NAME", self.name) # This will raise singleton error
        # filtered is used to filter the records
        # It can be called only with recordset containing records
        # You can use either just the field name in filtered which will check value eexisting or not.
        # In below case it will return records which have active set.
        # This will show in the Terminal that records are in active stage or not
        active_records = self.filtered('active')
        print("ACTIVE RECORDS", active_records)
        # 2) Way is to using lambda function where you can use proper conditions to filter records.
        # Another way of filtering the data in the module using lambda function in it.
        # Exercise-3 Q-19,Q-20 Filter the existing recordset with a condition. The condition should contain a field
        # and a value.
        female_records = active_records.filtered(lambda r: r.gender == 'female')
        male_records = active_records.filtered(lambda r: r.gender == 'male')
        print("FEMALE RECORDS", female_records)
        print("MALE RECORDS", male_records)

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
            print("Female IN ACT", fr in active_records)

        res = female_records not in active_records
        print("RES", res)

        # Exercise-3 Q-24. Get three different recordset where first one will have all the records of a model,
        # the second one will have few records of the model and third one will also have
        # few records of that model. The condition of the later two recordset should not be
        # same. Now check whether the later recordset are subset or superset of each other
        # or not. Also check whether the first recordset is a superset or subset or not.

        # < is used to check subset
        print(" Female is subset of male", female_records < male_records)
        # <= is used to check either subset or same set
        print(" Male is Subset of female OR SAME1", male_records <= female_records)
        print("Subset OR SAME2", active_records <= active_records)
        # > is used to check superset
        print(" Male is SUPER set of female", male_records > female_records)
        # >= is used to check superset or same set
        print(" Female is SUPER of Male set OR SAME 1", female_records >= male_records)
        print(" SUPER OR SAME 2", active_records >= active_records)
        # Exercise-3 Q-25 Get the union, intersection and difference of two recordsets.
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
            # print("O2M FIELD", patient.appointment_ids)
            # If there are multiple records you can not access the field directly.
            # print("Appointment FIELD",patient.appointment_ids # This will raise an error of singleton

        # You can use index in the recordset but if and only if there is a record
        # if patient.appointment_ids:
        #     print("O@M APPOINTMENT PATIENT", patient.appointment_ids[0].patient_name)

        # # ensure_one() is used to validate a single record
        patient.ensure_one()  # NO ERROR
        #patient.appointment_ids.ensure_one() # ERROR

        for patient in self:
            total = 0.0
        for medicines in patient.medicines_ids:
            total += medicines.total_price
        patient.total_price = total

        # Exercise-3 Q-21. From a recordset get two fields character and integer such that the result would
        # contain a single value which will be a concatenation of two fields mentioned above.
        merge_patient_name_age = patient.mapped(lambda a: f"{a.patient_name}-{a.age}")
        print(merge_patient_name_age)

        # Exercise-3 Q-22. From a recordset get a list of values in a specific field.
        record_list = patient.mapped('patient_name')
        print(record_list)

    # This is the Method of Medicine total tax &&&  calculate the tax without the other tax.
    # It will calculate total tax using a compute method.
    @api.depends('medicines_ids')
    def _cal_total_tax(self):
        for patient in self:
            total = 0.0
            for medicine in patient.medicines_ids:
                total += medicine.total_tax
            patient.total_tax = total

    @api.depends('medicines_ids')
    def _cal_total_tax_without_other_tax(self):
        for patient in self:
            total = 0.0
            for medicine in patient.medicines_ids:
                total += medicine.without_other_tax
            patient.without_other_tax = total

    #................... REFFFFFFFFFF METHOD....................

    # Ref Method using self.env.ref it will get the xml id from your model name hospital_management.
    # You Can do this by 2 method.
    # First is go to the settings, View and find your xml External Id.
    # Second is creating a function Check ORM of your model.
    def check_orm(self):
        search_var = self.env.ref('hospital_management.view_patient_form')
        print("search_var.............", search_var.type, "name----", search_var.name)

    # If you want to get a XML ID from the view than use this one.
    # It will get the XML model ID in the terminal. REFFFF Method Using ID.
    def check_orm(self):
        search_var = self.env.ref('hospital_management.view_patient_form').id
        print("search_var.............", search_var)

    #.................... Create Method...................

    # Create Method is Use to Create a Record in backend side when you click on the Check ORM,it will create a record
    # In this method we use dictionary and also use .id to showing a id of the new record.

    # Exercise-3 Q-26 Add a button on the form view when you click on this button it will create a
    # record on a new model which does not have a relation with the current model. CREATE METHOD
    def check_orm(self):
        create_var = self.env['hospital.patient'].create({
            "patient_name": 'Function Record',
            "age": 23,
        })
        print("Create var............", create_var.id)

        #...................... Write Method...................

        # Another way to update a record using a brw_Id of the record.
        # Create a method to Update the Record in the recordset using a ID & then update a record Using
        # a write method in it.

        # Exercise-3 Q-28. Add a button on the form view. When you click this button it should update a
        # field’s value of the current record.

        brw_id = self.env['hospital.patient'].browse(44)
        update = brw_id.write({
            "patient_name": 'Function Record Manually',
            "age": 33,
        })
        print("UPDATE............. ", update)

        #.....................Copy Method...............

        # In this Method also used a brw ID for copying a record.
        # brw_id.copy

        brw_id = self.env['hospital.patient'].browse(33)
        brw = brw_id.copy()
        print("COPY....................", brw)

        #...................Unlink Method..........

        # This Method delete a record using a brw ID.
        # Every time you have to give a new id bcz once it will delete you it can not be

        # brw_id=self.env['hospital.patient'].browse(68)
        # brw= brw_id.unlink()
        # print("UNLINK...............",brw)

        # Exercise-3 Q-39 Get a recordset of the current user without using the env parameter user.
        print("UID", self._uid)

        # In this Method using search in ORM to find the records according to the Condition
        # SEARCH METHOD

    def print_patient(self):
        search_var = self.env['hospital.patient'].search([('gender', '=', 'male')])
        print("Search Var........................", search_var)

        for rec in search_var:
            if rec in search_var:
                # print("Patient Name.....................", rec.patient_name, 'gender......', rec.gender)
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'type': 'rainbow_man',
                        'message': 'Record has been created successfully'
                    }
                }

        # TODO: Future development
        print("PRINT")
        print("SELFFFFFF", self)
        print("ENVIRONMENT", self.env)
        print("ENVIRONEMTN  ATTRS", dir(self.env))
        print("ARGS", self.env.args)
        print("CURSOR", self.env.cr)
        print("UID", self.env.uid)
        # Exercise-3 Q-13,14,15,16  User,Context,Company,Language
        print("USER", self.env.user)
        print("CONTEXT", self.env.context)
        print("COMPANY", self.env.company)
        print("COMPANIES", self.env.companies)
        print("LANG", self.env.lang)

    # appt_obj = self.env['hospital.appointment']
    # print("APPT OBJ", appt_obj)
    # depa_obj = self.env['hospital.department']
    # print("DEP OBJ", depa_obj)
    #
    # form_view_pat = self.env.ref('hospital.view_patient_form')
    # print("FORM VIEW PAT", form_view_pat)

    # Exercise-3 Q-40 Get a recordset of the user who created the record.
    # Exer-3 Q-27 Add a button on the form view on the page of a one2many field. When you click
    # this button it will add a record in the one2many field.

    def create_rec(self):

        vals1 = {
            'patient_name': 'kajal',
            'patient_id': 21,
            'gender': 'female',
            'blood_group': 'A+',
            'active': True,
            'age': 34,
            'birthdate': '1989-04-01',
            # 0 is used for creation
            # (0,0,{}) used to create record in O2M field
            # 'appointment_ids': [
            #     (0, 0, {
            #         'patient_id': 14,
            #         'patient_name': 'kervi',
            #
            #     }),
            #     (0, 0, {
            #         'patient_id': 32,
            #         'patient_name': 'Romil',
            #     })
            # ],
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

    # Exercise-3 Q-41 Add a user’s many2one field on your model. When a button is clicked by any
    # user, it should update this field with the current logged in user.

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
        # 5 is used to unlink all records .
        # (5,0,0) is used to unlink all records and keeps in the table.It is use for Many2Many..
        # 6 is used to link multiple records but overwrites existing ones
        # 6 first performs the 5 operation to remove existing records.
        # then uses 4 operation to link the new records
        vals = {
            'age': 29.0,
            'department_id': 4,
            # 'appointment_ids': [
            #     #  (5,0,0)
            #     #  (6,0,[1,2,3])
            #     #  (6,0,[8,19])
            #     (4, 1), (4, 2), (4, 3)
            # ]
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

        pat_rec = self.browse(239)
        print("\n PATIENT --------------------------", pat_rec)

        pat_dict = pat_rec.read(
            ['patient_name', 'age'], load ='')
        print("Patient DICT----------------------", pat_dict)

        # M2O will give a tuple containing id and name (if load =='_classic_read')
        # M2O will give you id (if load != '_classic_read')
        #, 'patient_id', 'appointment_ids', 'facility_ids'
        # print("DEPARTMENT", pat_dict[0]['department_id'])
        # # O2M  will give a list of ids
        # print("Appointment", pat_dict[0]['appointment_ids'])
        # # M2M will give a list of ids
        # print("ACT", pat_dict[0]['activity_ids'])
        # patient = self.browse([1, 2])
        # print("\nPatients--------------------------", patient)

    def copy_rec(self):
        default = {
            'patient_name': self.patient_name + ' (copy)',
            'email': False
        }
        new_rec = self.copy(default=default)

        print("\nNEW REC", new_rec)

        # Exercise-3 Q-18.Get the value of all predefined fields for a recordset containing one or more
        # records without using the ORM methods.

        # get_metadata() gives you the pre-defined fields / magic fields
        # It returns a dictionary containing id, create_date, create_uid, write_date, write_uid

        for patient in self:
            mt_dt = patient.get_metadata()
            print("MeTa DaTa >>>>>>>>>>>>>>>>>>>", mt_dt)

    # Exercise-3 Q-29 Add another button on the page of one2many field when you click on this button
    # it will remove one record but it will not remove it from the database. Use Unlink for it.
    def delete_rec(self):
        res = self.unlink()
        print("RES", res)


    # Default Method to add a validation Error

    # Exercise-4 8.Override unlink() method to avoid deletion if it’s not8. Override unlink() method to avoid deletion if it’s not in the first state of the state
    # field. I do validation on appointment can't delete once you add on form.

    # def unlink(self):
    #     if self.appointment_ids:
    #         raise ValidationError("You can not delete a patient with appointment!")
    #     return super().unlink()

    # def unlink(self):
    #             res = self.unlink()
    #             print("RES Records will be delete but keep in table", res)
        # 4 to link the records
        # (4,<id>)
        # 'facility_ids': [(4, 2), (4, 5)],


    # Exercise-3 Q-35. Fetch the no of records based on a condition with using search method.

    def search_rec(self):
        all_patient_name = self.search([])

        # Exercise-3 Q-38 Get all the records with specific fields without passing the domain. Sort the
        # records by name.

        # When you pass a blank domain it will return all the records.
        print("ALL PATIENTS", all_patient_name)

        # When you pass a condition in domain it will pass only matching records
        male_patient = self.search([('gender', '=', 'male')])
        print("MALE PATIENTS", male_patient)

        # When you pass offset it will skip no of records from the result
        offset_3_patient = self.search([], offset=3)
        print("SKIP 3 RECORDS", offset_3_patient)

        # When you pass limit it will limit the max no of records to fetch
        limit_4_patient = self.search([], limit=4)
        print("First 4 RECORDS", limit_4_patient)

        # Exercise-3 Q-34 Fetch 15 records from a model skipping first 5 records based on a condition and it
        # should be sorted by name.

        # When you pass offset and limit both the priority will be offset and then limit
        off_5_limit_15_patient_name = self.search([], offset=5, limit=15)
        print("SKIP 5 MAX 15 RECORDS", off_5_limit_15_patient_name)

        # When you pass order you can sort the records by a specific field
        sort_asc_patient_name = self.search([], order='patient_name')
        print("SHORT BY NAME<", sort_asc_patient_name)

        # Exercise-3 Q-23 Sort a recordset in a descending order with a field other than name. The action
        # should be performed on a recordset only.

        # When you pass desc after the field it will sort in descending order
        sort_desc_age = self.search([], order='age desc')
        print("SHORT BY AGE< DESC", sort_desc_age)

        # When you pass offset, limit and order the priority goes to order then offset and then limit
        sort_asc_patient_name = self.search([], offset=2, limit=4, order='patient_name')
        print("SHORT BY NAME< OFFSET LIMIT", sort_asc_patient_name)

        # When you pass count=True it returns no of records rather than a recordset
        no_of_patient = self.search([], count=True)
        print("TOTAL PATIENT", no_of_patient)
        no_of_female_patient_name = self.search([('gender', '=', 'female')], count=True)
        print("FEMALE PATIENT", no_of_female_patient_name)

        # Exercise-3 Q-36 Get the no of records based on a condition.
        ## search_count
        no_of_patient = self.search_count([])
        print("TOTAL PATIENT", no_of_patient)
        no_of_female_patient_name = self.search_count([('gender', '=', 'female')])
        print("FEMALE PATIENT", no_of_female_patient_name)

        ### search_read
        # patient_name_lst = self.search_read(
        #     fields=['patient_name', 'age', 'department_id', 'appointment_ids', 'facility_ids'])
        # print("SEARCH READ Patient", patient_name_lst)
        # patient_name_lst_2 = self.search_read(
        #     fields=['patient_name', 'age', 'department_id', 'appointment_ids', 'facility_ids'],
        #     order='patient_name')  # Exercise-3 Q-35 without using search method.len(patient_name_lst_2)
        # print("SEARCH READ PATIENT", patient_name_lst_2, "no of record", len(patient_name_lst_2))


    # Exercise-4 Q-1 Override create method to create a record in another model.
    # Exercise-4 Q-24. Create a sequence and assign it on creation of the record.
    @api.model
    def create(self,vals):
        """
               Overridden create() method to have automated patient code
               ---------------------------------------------------------
               @param self: object pointer
               @param vals_lst: List of dictionaries containing fields and values
               return: Recordset containing newly created record(s)
               """

        # when create New Patient sequence according to their sequence automatic.
        # Next_by_code method
        if vals.get('patient_code'):
            vals['patient_code'] = 'New Patient'
        if vals.get('reg_no', _('New')) == _('New'):
            vals['reg_no'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')


        #This is to Override a Patient name while creating a new patient
        # It will take 4 letters of patient of while creating.
        # Second way to use the sequence is next_by_id

        if vals.get('patient_name'):
            vals['patient_code'] = vals['patient_name'][:4].upper()
        res = super(Patient,self).create(vals)
        print("____________Code Generated",res)
        return res

    # One way to use the sequence is next_by_code
    # For this you just need the object and code of the sequence
    # if vals_lst.get('patient_name'):
    #     vals_lst['patient_code'] = vals_lst['patient_name'][:2].upper()
    # return super().create(vals_lst)


    # Exercise-4 Q-4 Override write() method to update the records.
    def write(self,vals):
        if vals.get('patient_name'):
            vals['patient_code'] = vals['patient_name'][:4].upper()
        return super().write(vals)

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """
        Overridden Search method to fetch inactive records as well
        ----------------------------------------------------------
        @param self: object pointer
        @param args: Domain / List of conditions
        @param offset: no of records to skip
        @param limit: Max nno of records
        @param order: field name for sorting
        @param count: True/False
        :return : Recordset if count=False else no of records
        """
        args = ['|', ('active', '=', False), ('active', '=', True)] + args
        print("__________________________________Search successfully")

        return super().search(args, offset=offset, limit=limit, order=order, count=count)

    # def unlink(self):
    #     """
    #     Overridden unlink() method to check if the appointment are existing it should not allow to delete
    #     -----------------------------------------------------------------------------------
    #     @param self: object pointer
    #     :return : True
    #     """
        # if self.appointment_ids:
        #     raise ValidationError("You can not delete a patient with appointment!")
        # print("______________________Return statement,deleted successfully")
        # return super().unlink()

    # Exercise-4 5,6. Override copy() method to remove one of the existing fields and add another value.
    def copy(self, default=None):

        default = {
            'patient_name': self.patient_name + '- Copy'
        }
        print("__________________________________Return Statement,copy successfully")
        return super().copy(default=default)


    # # Exercise-4 7.Override copy() method and have the state field not copied and bring back to the fiirst state in the selection.
    # @api.model
    # def copy(self, default=None):
    #     original_state = self.state
    #
    #     default = {
    #              'state' : self.state + 'admit'
    #     }
    #     if original_state in ('confirmed', 'done'):
    #         default['state'] = 'waiting'
    #     else:
    #         default['state'] = original_state
    #
    #     return super().copy(default=default)

    # Exercise-4 12.Override default_get method to add default fields when the record is created.

    @api.model
    def default_get(self, fields_list):

            print("FIELDS LIST", fields_list)
            res = super().default_get(fields_list=fields_list)
            # print("___________________RES", res)
            res.update({'url': 'www.skyscendbs.com'})
            print("_________________UPDATE RES", res)
            res['age'] = 22
            res['phone_number'] = 123456890

            # To GET A Default appointment in M2O field in the Model
            # res['appointment_ids'] = [(0,0,{'patient_name':'leelaaaa','email':'leela@gmail.com'}),
            #                           (0,0,{'patient_name':'Anjuuuu','email':'anju@gmail.com'})]
            print('________Default Value of Age, phone no,URL', res)
            return res

    # Exercise-4 Q-26 Add an SQL constraint to check a field’s value is not greater than a specific
    # number.

    @api.constrains('age', 'gender')
    def check_patient_age(self):
            """
            Object Constraint used to check the age as per the gender
            ---------------------------------------------------------
            """
            for patient in self:
                if patient.gender == 'male' and patient.age < 10:
                    raise ValidationError('Males should be 12 years old to get admitted!')
                if patient.gender == 'female' and patient.age < 12:
                    raise ValidationError('Females should be 12 or more to get admitted!')

    # Exercise-4 25.Create a sequence and assign it’s value on a button click.
    def assign_sequence(self):
        sequence_obj = self.env['ir.sequence']
        self.reg_no = sequence_obj.next_by_code('hospital.patient') or _('New')


    # Exercise-5 Q-33 Add a dropdown on the kanban view it will open the records of the one2many
    # field.
    def open_one2many(self):
        self.ensure_one()
        return {
            'name': 'One2Many Records',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'hospital.medicines',
            'domain': [('medicines_id', '=', self.id)],
        }
    # Exercise-5 Q-34. Add a dropdown on the kanban to call a method of the model which will update
    # the value of a field in the record. Method for the kanban view in dropdown list.

    def action_confirm(self):
        self.state = 'draft'