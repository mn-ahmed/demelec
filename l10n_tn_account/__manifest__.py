# -*- encoding: utf-8 -*-

{
    "name": "Tunisia - Accounting",
    "version": "16.0.1.0",
    "author": "Ahmed Mnasri",
    "license": "LGPL-3",
    "category": 'Accounting/Localizations/Account Charts',
    "description": """
This is the base module to manage the accounting chart for Tunisia.
=================================================================
""",
    "depends": ['base', 'account'],
    "init_xml": [],
    "data": [
        'data/l10n_tn_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_data.xml',
        'data/account_tax_group_data.xml',
        'data/account_tax_data.xml',
        'data/l10n_chart_config_data.xml',

        ],
    'images': ['static/description/Banner.png'],
}
