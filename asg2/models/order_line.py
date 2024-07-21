from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class OrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_booking = fields.Float(string='Qty Booking', default=0.00)
    product_template_id = fields.Many2one('product.template',compute='_compute_product_template_id', string='product_template_id')

    
    @api.depends('product_id')
    def _compute_product_template_id(self):
        for record in self:
            record.product_template_id = record.product_id.product_tmpl_id

    @api.onchange('qty_booking','product_uom_qty')
    def _onchange_qty_booking(self):
        for record in self:
            if record.order_id.is_booking == True:
                record.product_uom_qty = record.qty_booking
                record.product_template_id.qty_order_line = record.qty_booking     

    # Not yet active
    @api.constrains('order_line')
    def _check_booking_order_limit(self):
        config = self.env['booking.configuration'].search([[(self.product_template_id, '=', 'id')]])
        if config:
            for order in self:
                max_qty = self.product_template_id.qty_available * self.product_template_id.qty_limit / 100
                if order.product_template_id.qty_booking > max_qty :
                    raise ValidationError('Total booking quantity for this product has reached the maximum limit.')


    
    

