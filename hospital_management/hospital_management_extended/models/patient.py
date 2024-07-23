from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    # If you use only _inherit it will add / modify in to existing
    _inherit = 'hospital.patient'

    height = fields.Float('Height(cm)')
    weight = fields.Float('Weight(kg)')
    extra_notes = fields.Html('Extra Notes')

    # This is New Field Added for calculate a BMI
    # For a more example, let's use height = 170 cm and weight = 55 kg:

    # bmi = round(55 / ((170 / 100) ** 2), 2)
    # 170 / 100 = 1.7 meters
    # (1.7) ** 2 = 2.89
    # 55 / 2.89 = 19.03
    # round(19.03, 2) = 19.03
    # This gives a BMI of 19.03, which is within the normal range for adults.
    bmi = fields.Float(' Body Mass Index(BMI)', readonly=True)

    def print_patient(self):
        super().print_patient()
        print(" **************************** NEW METHOD")

    # Exercise-6 Q-5 Modify an existing onchange method to be also called from an additional field and
    # use this field in the logic to change other field’s value.
    @api.onchange('height', 'weight')
    def _onchange(self):
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 2) \
            if self.height and self.weight else 0.0

    #Exercise-6 Q-6 Modify an existing constraint method to be also called from an additional field
    # with an additional logic.

    @api.constrains('height')
    def check_patient(self):
        for patient in self:
            if patient.height:
                if patient.height < 100:
                    raise ValidationError('Patient height at least 100 cm for admited.')
                elif patient.height > 250:
                    raise ValidationError('Patient height more than 250 cm.')
            else:
                raise ValidationError('Height must be provided for patient admission.')


    # @api.multi
    # def update_patient(self):
    #     self.ensure_one()  # Ensure this method is called on a single record
    #     self.existing_method()    # Call the existing method
    #
    #     vals = {
    #     'patient_name': 'Hardik',
    #     'patient_id': 20,
    #     'gender': 'male',
    #     'blood_group': 'A',
    #     'active': True,
    #     'age': 29,
    #     'birthdate': '2004-05-17',
    # }

