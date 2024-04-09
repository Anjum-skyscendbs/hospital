{
    'name': 'Hospital Management',
    'description': 'This module is used to manage Patient Information',
    'author': 'Anjum Nakani',
    'website': 'https://www.skycendbs.com',
    'version': '1.0',
    'depends': ['base'],
    'data':[
        'security/hospital_security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/appointment_view.xml',
        'views/facility_view.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True,

}
