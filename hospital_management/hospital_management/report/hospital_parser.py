from odoo import models, fields, api

class HospitalReport(models.AbstractModel):
    _name = 'report.hospital_management.report_patient'  # name of your reports
    _description = 'Hospital Management Profile Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n\n\nDOC IDS", docids)
        print("SELF", self.ids)
        print("CONTEXT", self._context)
        print("DATA", data)
        docs = self.env['hospital.patient'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'hospital.patient',
            'data': data,
            'docs': docs,
            'test': 'TEST VARIABLE',
            'get_total_price': self._get_total_price,
        }

    @api.model
    def _get_total_price(self, price):
        total_price = 0.0
        for dtl in price:
            total_price += dtl.gst + dtl.sgst + dtl.other_tax
        return total_price




