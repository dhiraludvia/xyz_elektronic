# -*- coding: utf-8 -*-
{
    'name': "Inventory Booking Report",

    'summary': """
        Add report (pivot,pdf,excel) to Inventory module""",

    'author': "My Company",
    
    'category': 'Inventory',
    'version': '0.1',
    'application': True,

    'depends': ['base','asg2','stock','report_xlsx'],

    'data': [
        'security/ir.model.access.csv',
        'views/edit_inventory.xml',
        'views/inventory_pivot.xml',
        'wizard/inventory_bookingwz.xml',
        'wizard/inventory_bookingwz_xlsx.xml',
        'report/report.xml',
        'report/report_inventory_booking_template.xml',
        'report/report_inventory_bookingwz_pdf.xml',
    ],
    
}
