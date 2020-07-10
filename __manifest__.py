# -*- coding: utf-8 -*-
{
    'name': "E-commerce show tax included or excluded",

    'summary': """
        Show if taxes are included/excluded next to price
        """,

    'description': """
        The prices on e-commerce could be tax included or tax excluded.
        This information is not shown to the customer
        who finds out only at the end of the process.
        This module shows next to the product price if the tax is included
        or not.
        You can activate/deactivate this function both in product catalogue 
        or on product page by selecting the option in customise menu
    """,

    'author': "Alberto Carollo",
    'website': "https://github.com/baba75",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'e-commerce',
    'version': '12.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}