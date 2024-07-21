from odoo import models, fields, api, _

class BookingOrder(models.Model):
    _inherit = 'sale.order'

    is_booking = fields.Boolean(string='Booking Order')
    state = fields.Selection(selection_add=[('booking','Booking')], ondelete={'booking':'cascade'})

            
    @api.model
    def create(self, vals):
        res = super(BookingOrder, self).create(vals)
        context = self._context or {}
        if context.get('default_is_booking'):
            res.name = self.env['ir.sequence'].next_by_code('referensi.bookingorder')
            res.state='booking'
        return res
            
