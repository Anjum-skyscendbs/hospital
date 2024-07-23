from odoo import models, fields, api


class SubFacility(models.Model):
    # For Delegate Inheritance _inherits can be used.
    # The _inehrits takes a dictionary.
    # The key will be the name of the model.
    # The value will be an M2O field for the same model in current model.
    _inherits= {'hospital.facility': 'facility_id'}
    _name = 'hospital_management.sub.facility'
    _description = 'Hospital Management Sub Facility'
    _rec_name = 'sub_faci_name'

    # The M2O field for the parent model for delegation.
    # It must have the required=True and ondelete='cascade'
    facility_id = fields.Many2one('hospital.facility', 'Facility', required=True, ondelete='cascade')
    sub_faci_name = fields.Char('Sub Facility Name')
    sub_faci_code = fields.Char('Sub Faci Code')


class SubFacility2(models.Model):
    # For Delegate Inheritance delegate=True can also be used.
    _name = 'hospital_management.sub.facility2'
    _description = 'Hospital Management Sub Facility2'
    _rec_name = 'sub_faci_name'

    # The M2O field for the parent model for delegation.
    # It will have delegate=True instead of _inherits
    # It must have the required=True and ondelete='cascade'
    facility_id = fields.Many2one('hospital.facility',
                                  'Facility',
                                  delegate=True,
                                  required=True,
                                  ondelete='cascade')
    sub_faci_name = fields.Char('Sub Facility Name')
    sub_faci_code = fields.Char('Sub Faci Code')