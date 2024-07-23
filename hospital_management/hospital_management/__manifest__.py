{
    'name': 'Hospital Management',
    'description': 'This module is used to manage Patient Information',
    'author': 'Anjum Nakani',
    'sequence': -100,
    'website': 'https://www.skycendbs.com',
    'version': '1.0',
    'depends': ['base','web'],
    'data':[
        'security/hospital_security.xml',
        'security/ir.model.access.csv',
        'data/patient_sequence.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/department_view.xml',
        'views/facility_view.xml',
        'views/prescription_view.xml',
        'views/diseases_view.xml',
        'views/medicines_view.xml',
        'wizard/update_charges_wiz_view.xml',
        'report/patient_analysis_view.xml',
        'views/report_patient_template.xml',
        'report/reports.xml',
        'wizard/patient_report_wiz_view.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'hospital_management/static/src/scss/test_style.scss'
        ],
    },

    'auto_install': False,
    'installable': True,
    'application': True,

}
