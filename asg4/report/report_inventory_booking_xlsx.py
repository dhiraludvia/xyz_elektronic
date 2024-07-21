from odoo import models

class BookingOrderXlsx(models.AbstractModel):
    _name = 'report.asg4.report_inventory_booking_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Report Inventory Booking XLSX'

    def generate_xlsx_report(self, workbook, data, orders):
        sheet = workbook.add_worksheet('Inventory Booking Report')

        # Header
        header_format = workbook.add_format({'font_size':14, 'bold': True, 'align': 'center', 'valign': 'vcenter'})
        sheet.set_row(0, 30, header_format)
        sheet.write(2, 0, 'Delivery Address', header_format)
        sheet.write(3, 0, 'Scheduled Date', header_format)
        sheet.write(2, 4, 'Source Document', header_format)
        sheet.write(3, 4, 'Booking Order', header_format)

        # Data
        row = 0
        for order in orders:
            col = 1
            sheet.write(row, col + 1, order.name)
            sheet.write(row + 2, col, order.partner_id.name)
            sheet.write(row + 3, col, order.scheduled_date.strftime('%Y-%m-%d') if order.scheduled_date else '')
            sheet.write(row + 2, col + 5, order.origin)
            sheet.write(row + 3, col + 5, order.is_booking)
            row += 1

        # Table 2: Order Lines
        row += 5
        sheet.write(row, 0, 'Product', header_format)
        sheet.write(row, 3, 'Demand', header_format)
        sheet.write(row, 4, 'Reserved', header_format)
        sheet.write(row, 5, 'Done', header_format)

        row += 1
        for order in orders:
            for line in order.move_ids_without_package:
                col = 0
                sheet.write(row, col, line.product_id.name)
                sheet.write(row, col + 3, line.product_uom_qty)
                sheet.write(row, col + 4, line.forecast_availability)
                sheet.write(row, col + 5, line.quantity_done)
                row += 1

        sheet.set_column(0, 0, 30)  
