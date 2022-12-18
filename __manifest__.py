# -*- coding: utf-8 -*-
{
    'name': "libreria",
    'summary': """libreria""",
    'description': """
        this is a module for a library:
    """,
    'author': "Diego",
    'website': "https://github.com/Diegobc2323",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
    'qweb': ['static/src/description/icon.svg']
}