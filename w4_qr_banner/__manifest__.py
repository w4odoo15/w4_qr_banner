# -*- coding: utf-8 -*-
{
    'name': "Banner ad on Swiss QR-invoices",

    'summary': """
       Lets businesses place customised ads on Swiss QR-invoices""",

    'description': """
        Invoice, Accounting, Ads
    """,

    'author': "W4 Services AG",
    'website': "https://just-odoo.agency/",

    'category': 'Accounting',
    'price': '450',
    'currency': 'EUR',
    'license': 'OPL-1',
    'version': '17.0.1.1',

    'depends': ['base','account', 'l10n_ch'],

    'data': [
        'views/company.xml',
        'views/qr_template.xml',
    ],
    'images': ['static/description/cover.gif']
}
