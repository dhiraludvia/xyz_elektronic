from odoo import models, fields, api,_
from datetime import timedelta

class HistoryBookingOrder(models.Model):
    _inherit = 'sale.order'

    sale_order_number = fields.Char(string='Sale Order Number')

    def _cancel_unprocessed_booking(self):
        booking_to_cancel = self.search([
            ('is_booking', '=', True),
            ('date_order', '<=', fields.Datetime.to_string(fields.Datetime.now() - timedelta(days=3)))
        ])
        booking_to_cancel.action_cancel()

    def action_convert_to_rfq(self):
        for record in self:
            if record.is_booking:
                sale_order_number = record.name
                record.write({
                    'is_booking': True,
                    'state': 'draft',
                    'name': self.env['ir.sequence'].next_by_code('sale.order'),
                    'sale_order_number': sale_order_number,
                })


class BookingConfiguration(models.Model):
    _name = 'booking.configuration'
    _description = 'booking.configuration'

    product_id = fields.Many2one('product.template', 'Product')
    max_booking = fields.Float('Max Booking per Booking Order')
    qty_limit = fields.Float('Qty Limit')
    sign = fields.Char('sign')


    @api.onchange('product_id')
    def _compute_qty_limit(self):
        try:
            self.qty_limit = self.product_id.qty_available / self.product_id.qty_available * 100
        except ZeroDivisionError:
            self.sign = 'Product is out of stock'
            self.qty_limit = 0
        except Exception:
            self.sign = 'Error'
        else:
            self.sign = ''



