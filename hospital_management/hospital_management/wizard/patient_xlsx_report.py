from odoo import models, fields, api
import xlsxwriter
import base64

class PatientReportXlsx(models.TransientModel):
    _name = 'patient.report.xlsx'
    _description = 'Patient Excel Report'

    patient_ids = fields.Many2many('hospital.patient', string='Patients')


    @api.model
    def default_get(self, fields):
        res = super(PatientReportXlsx, self).default_get(fields)
        return res

    def print_xlsx(self):
        """
        This Method is used to print xlsx report.
        ----------------------------------------
        @param self: object pointer
        """
        attachment_obj = self.env['ir.attachment']
        wb = xlsxwriter.Workbook('/tmp/patient_report.xlsx')

        # Define formats
        header_format = wb.add_format({
            'bold': True,
            'align': 'center',
            'bg_color': '#D9EAD3',
            'border': 4,
            'font_size': 13
        })
        # subheader_format = wb.add_format({
        #     'bold': True,
        #     'align': 'center',
        #     'bg_color': '#F9CB9C',
        #     'border': 1,
        #     'font_size': 10
        # })

        # total_format = wb.add_format({
        #     'bold': True,
        #     'bg_color': '#D9EAD3',
        #     'border': 1,
        #     'align': 'right',
        #     'font_size': 10
        # })

        # Iterate over patients
        for patient in self.patient_ids:
            sheet = wb.add_worksheet(patient.patient_name)

            # Set column widths
            sheet.set_column('A:A', 20)
            sheet.set_column('B:B', 15)
            sheet.set_column('C:C', 15)
            sheet.set_column('D:D', 15)
            sheet.set_column('E:E', 15)
            sheet.set_column('F:F', 25)
            sheet.set_column('G:G', 20)
            sheet.set_column('H:H', 20)
            sheet.set_column('I:I', 20)
            sheet.set_column('J:J', 20)
            sheet.set_column('K:K', 20)
            sheet.set_column('L:L', 20)

            # Headers
            sheet.merge_range(5, 4, 5, 5, 'Patient Report', header_format)
            sheet.write(7, 0, 'Patient Name', header_format)
            sheet.write(7, 1, patient.patient_name)

            # sheet.write(8, 0, 'Department', header_format)
            # sheet.write(8, 1, patient.department_id.department)

            sheet.write(8, 0, 'Gender', header_format)
            sheet.write(8, 1, patient.gender)

            # Write column headers
            sheet.write(12, 0, 'Medicine Name', header_format)
            sheet.write(12, 1, 'GST', header_format)
            sheet.write(12, 2, 'SGST', header_format)
            sheet.write(12, 3, 'Other Tax', header_format)
            sheet.write(12, 4, 'Total Tax', header_format)
            sheet.write(12, 5, 'Without Other Tax', header_format)
            sheet.write(12, 6, 'Total Price', header_format)
            sheet.write(12, 7, 'Tax Percentage', header_format)

            # Write data rows
            row = 13
            for medicines in patient.medicines_ids:
                sheet.write(row, 0, medicines.medicines_id.medicines_name)
                sheet.write(row, 1, medicines.gst)
                sheet.write(row, 2, medicines.sgst)
                sheet.write(row, 3, medicines.other_tax)
                sheet.write(row, 4, medicines.total_tax)
                sheet.write(row, 5, medicines.without_other_tax)
                sheet.write(row, 6, medicines.total_price)
                sheet.write(row, 7, medicines.tax_perc)
                row += 1

        wb.close()

        # Opening XLSX File from tmp directory
        f1 = open('/tmp/patient_report.xlsx', 'rb')

        # Read the Data of XLSX
        xlsx_data = f1.read()

        # Encode It Using base64
        buf = base64.b64encode(xlsx_data)

        # # Create A Record Of that attachment
        doc = attachment_obj.create({'name': '%s.xlsx' % ('Patient Report'),
                                     'datas': buf,
                                     'res_model': 'patient.report.xlsx',
                                     'store_fname': '%s.xlsx' % ('Patient Report'),
                                     })


        # Return A URL Action Of Attachment Record
        return {'type': 'ir.actions.act_url',
                'url': 'web/content/%s?download=true' % (doc.id),
                'target': 'current'
                }
