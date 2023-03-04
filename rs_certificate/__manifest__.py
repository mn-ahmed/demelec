# -*- coding: utf-8 -*-
{
    'name': "Payement - retenue à la source",

    'summary': """
       Imprission de certificat de retenue à la source""",
    'description': """
        Model de Certificat de retenue à la source Tunisienne
    """,
    'author': "Ahmed Mnasri",
    'website': "http://polyline.xyz",
    'category': 'accounting',
    'version': '1.2.1',
    'depends': ['account',
                'account_check_printing'
                ],
    'data': [
        # 'security/ir.model.access.csv',
        'data/account_rs_data.xml',
        'views/rs_report_templates.xml',
        'views/account_payment_views.xml',
        'views/account_journal_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
    "price": 30,
    "currency": 'EUR',
    'images': ['static/description/banner.png'],
}
