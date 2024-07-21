# -*- coding: utf-8 -*-
{
    'name': "XYZ Corporation",

    'summary': """
        Electronic goods distribution company""",
    
    'category': 'Sales',
    'version': '0.1',
    'application': True,

    'depends': ['base','asg2','asg4','purchase'],

    'data': [
        'security/security_sales.xml',
        'security/security_purchase.xml',
        'security/security_inventory.xml',
        'views/edit_sales.xml',
        'views/edit_purchase.xml',
        'views/edit_inventory.xml',
    ],

}