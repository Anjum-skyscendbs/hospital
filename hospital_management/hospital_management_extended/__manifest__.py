{
    'name': 'Hospital Management Extended',
    'description': 'This module is used to manage patient Information',
    'author': 'Anjum Nakani',
    'website': 'https://www.skyscendbs.com',
    'version': '1.0',
    'depends': ['base','web','hospital_management'],
    'data': [
        'security/hospital_security.xml',
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/patient_view.xml',
    ],
    'auto_install': False,
    'installable':True,
    'application': True,
}