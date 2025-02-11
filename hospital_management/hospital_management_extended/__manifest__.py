{
    'name': 'Hospital Management Extended',
    'description': 'This module is used to manage patient Information',
    'author': 'Anjum Nakani',
    'website': 'https://www.skyscendbs.com',
    'sequence': -90,
    'version': '1.0',
    'depends': ['base','web','mail','hospital_management'],
    'data': [
        'security/hospital_security.xml',
        'security/ir.model.access.csv',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/sub_facility_view.xml',
        'wizard/update_charges_wiz_view.xml',
        'views/report_patient_template.xml',

    ],
    'auto_install': False,
    'installable':True,
    'application': True,
}