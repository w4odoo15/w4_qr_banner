# -*- coding: utf-8 -*-
{
    'name': "QR Banner for Swiss Invoice",

    'summary': """
       Lets businesses place customised ads on Swiss QR-invoices""",

    'description': """
        Invoice, Accounting, Ads
    """,

    'author': "W4 Services AG",
    'website': "https://just-odoo.agency/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'price': '450',
    'currency': 'EUR',
    'license': 'OPL-1',
    'version': '17.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'l10n_ch'],

    # always loaded
    'data': [
        'views/company.xml',
        'views/qr_template.xml',
    ],
    'images': ['static/description/cover.gif']
}
