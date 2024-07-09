{
    'name': 'Sale Discount Amount',
    'version': '0.1',
    'description': 'Adds discount amount field to sale order lines',
    'sequence': -70,
    'author':'Skyscend Business Solutions',
    'website':'http://www.skyscendbs.com',
    'depends': ['sale','stock'],
    'data': [
        'views/sale_order_line_view.xml',
        'views/account_move_line_view.xml',

    ],
    'auto_install': False,
    'installable': True,
    'application':True,
}
