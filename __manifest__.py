# -*- coding: utf-8 -*-
{
    'name': "app_test name",

    'summary': """
        Hello, this is summary
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "This is author",
    'website': "http://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.69',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    'application': True,
}
