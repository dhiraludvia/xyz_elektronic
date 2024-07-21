from odoo import models, fields, api

class ReportInventoryBookingWz(models.TransientModel):
    _name = 'report.inventory.bookingwz'
    _description = 'Report Inventory Booking Wizard'

    from_date = fields.Date(string='From Date', required=True)
    to_date = fields.Date(string='To Date', required=True)

    def action_inventory_booking_report(self):
        report = []
        from_dateorder = self.from_date
        to_dateorder = self.to_date
        if from_dateorder:
            report += [('scheduled_date','>=',from_dateorder)]
        if to_dateorder:
            report += [('scheduled_date','<=',to_dateorder)]
        new_report = self.env['stock.picking'].search_read(report)
        detail_report = self.env['stock.picking'].search_read([])

        data = {
            'form' : self.read(0),
            'generate_report' : new_report,
            'detail_report' : detail_report
        }
        report_action = self.env.ref('asg4.action_report_inventory_bookingwz').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action
    
    