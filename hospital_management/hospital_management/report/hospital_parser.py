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
            'get_gst': self._get_gst,
            'get_sgst': self._get_sgst,
            'get_other_tax': self._get_other_tax,
            'get_total_tax': self.get_total_tax,
            'get_without_other_tax': self._get_without_other_tax,
            'get_total_price': self._get_total_price,
        }


    ### Here is the Method for Printing a report in the Template.
    ### Method for gst, sgst, other tax,total price,without other tax and total tax.
    ### You can see in the below code.

    @api.model
    def _get_gst(self, medicines_id):
        return sum(medicine.gst for medicine in medicines_id)

    @api.model
    def _get_sgst(self, medicines_id):
        return sum(medicine.sgst for medicine in medicines_id)

    @api.model
    def _get_other_tax(self, medicines_id):
        return sum(medicine.other_tax for medicine in medicines_id)

    @api.model
    def _get_total_price(self,medicines_id):
        return sum(medicine.total_price for medicine in medicines_id)

    @api.model
    def _get_without_other_tax(self,medicines_id):
        return sum(medicine.without_other_tax for medicine in medicines_id)

    @api.model
    def get_total_tax(self, medicines_id):
        total_tax = sum(medicines.total_tax for medicines in medicines_id)
        return total_tax

