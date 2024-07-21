# -*- coding: utf-8 -*-
{
    'name': "History Booking Order",

    'summary': """
        Add menu History Booking Order on Sales module""",

    'author': "My Company",
    
    'category': 'Sales',
    'version': '0.1',
    'application': True,

    'depends': ['base','sale_management','point_of_sale','product'],

    'data': [
        'security/ir.model.access.csv',
        'data/cron_jobs.xml',
        'data/booking_order_sequence.xml',
        'views/booking_order.xml',
        'views/history_booking.xml',
        'views/product_template.xml',
        'views/booking_configuration.xml',

    ],
    
}
