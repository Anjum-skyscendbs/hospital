{
    'name': 'Hr Employee Aadhaar No',
    'version': '0.1',
    'description': "This Module is used to change the functionalities of hr module",
    'author': 'Skyscend Business Solutions',
    'sequence': -60,
    'website': 'http://www.skyscendbs.com',
    'depends': ['hr'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_employee_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable':True,
}
