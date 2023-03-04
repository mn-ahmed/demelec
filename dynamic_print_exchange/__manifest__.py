# -*- coding: utf-8 -*-
# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': "Dynamic Print bill of exchange",
    'version': "16.0.1.0.0",
    'author': "Ahmed Mnasri",
    'license': "OPL-1",
    'live_test_url': '',
    'images': ['static/description/banner.gif'],
    'depends': ['base', 'account',
                'account_check_printing',
                'l10n_tn_base',
                ],
    'data': [
        'security/ir.model.access.csv',
        'data/account_exchange_data.xml',
        'views/exchange_configuration_views.xml',
        'views/account_payment_views.xml',
        'report/exchange_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    "price": 25,
    "currency": 'EUR',
    'category': "Accounting",
}
