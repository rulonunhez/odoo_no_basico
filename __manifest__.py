# -*- coding: utf-8 -*-
{
    'name': "odoo_basico",

    'summary': """
        Segundo proxecto de pycharm e odoo""",

    'description': """
        Probarase a vista tree
    """,

    'author': "Raul",
    'website': "http://www.edu.xunta.gal/centros/iesteis",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/informacion.xml',
        'views/suceso.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
