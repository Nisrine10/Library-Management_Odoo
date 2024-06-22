# -*- coding: utf-8 -*-
{
    'name': "Library_management",

    'summary': """
        Manage You library with Nisrine""",

    'description': """
        Manage library books, authors, categories, and borrowings.
    """,

    'author': "Nisrine",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/category_view.xml',
        'views/author_view.xml',
        'views/borrower_view.xml',
        'views/loan_view.xml',
        #'views/email_templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
