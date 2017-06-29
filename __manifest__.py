# -*- coding: utf-8 -*-
{
    'name': "Service Catalogue",

    'summary': """
        Sevice Catalogue
    """,

    'description': """
        Service Catalogue pour la gestion des tâches reccurentes Mitantana.
    """,

    'author': "Appy Solutions",
    'website': "http://www.appy.solutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/service_catalogue_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}