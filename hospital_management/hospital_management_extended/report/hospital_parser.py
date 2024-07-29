from odoo import models,api

class HospitalReport(models.AbstractModel):

    _inherit = 'report.hospital_management.report_patient'

    @api.model
    def _get_report_values(self,docids,data=None):
        res = super()._get_report_values(docids,data=data)
        res.update({
            'Name':'SkyScend Business Pvt Ltd',
            'Position':'Anjum Nakani'
        })
        return res


