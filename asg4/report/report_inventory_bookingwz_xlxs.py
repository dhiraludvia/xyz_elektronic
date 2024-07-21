from odoo import models

class BookingOrderWizardXlsx(models.AbstractModel):
    _name = 'report.report_inventory_bookingwz_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, reports):
        obj = data['reports']
        sheet = workbook.add_worksheet('Wizard Booking Order')
        bold = workbook.add_format({'bold': True})
        
        # Write headers
        headers = ['No. Booking Order', 
                   'Customer', 
                   'Transaction Date', 
                #    'Product',
                #    'Quantity', 
                   ]
        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header, bold)
        
        row = 1
        for x in obj:
            col = 0
            sheet.write(row, col, x['origin'])
            col += 1
            sheet.write(row, col, x['partner_id'][1] if x['partner_id'] else '')
            col += 1
            sheet.write(row, col, x['scheduled_date'])
            col += 1


            # Fetch details of each booking_line_ids
            # for detail_id in x['booking_line_ids']:
            #     detail = self.env['saleorderedit2.bookingorderline'].browse(detail_id)
            #     sheet.write(row, col, detail.product_id.name if detail.product_id else '')
            #     col += 1
            #     sheet.write(row, col, detail.product_uom_qty)
            #     col += 1
            #     row += 1  # Move to the next row for each detail
            #     col = 4  # Reset to the column after 'Total Sales' for new detail

            # Ensure to handle cases where there are no details
            # if not x['booking_line_ids']:
            #     row += 1 
