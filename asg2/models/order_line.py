from odoo import models, fields, api, _
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

    
    @api.onchange('product_id', 'qty_booking', 'price_unit')
    def _onchange_is_booking(self):
        for line in self:
            if line.product_id:
                price = line.product_id.list_price
                if line.order_id.is_booking:
                    line.price_unit = price * 1.1
                else:
                    line.price_unit = price
            
                
    @api.constrains('product_uom_qty')
    def _check_product_uom_qty(self):
        for record in self:
            if record.product_id and record.product_id.qty_available == 0:
                raise ValidationError(_('Booking for "%s" currently out of stock. Please make a Request for Purchase first.') % record.product_id.name)
            elif record.product_id and record.product_uom_qty > record.product_id.qty_available:
                raise ValidationError(_('Booking for "%s" reaching the maximum quantity limit. please reduce the order.') % record.product_id.name)

