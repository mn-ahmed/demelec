# -*- coding: utf-8 -*-
{
    'name': "l10n_tn_base",

    'summary': """
       This module may used by other modules """,

    'description': """
       
    """,
    'author': "Ahmed Mnasri",
    'license': "LGPL-3",
    'website': "http://polyline.xyz",
    'category': '',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
