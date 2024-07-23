from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.template'
    
    qty_order_line = fields.Float(string='Quantity Order Line')
    qty_booking = fields.Float(compute='_compute_qty_booking', string='Quantity Booking')
    qty_available_after_booking = fields.Float( string='Quantity Avaliable After Booking')
    
    @api.depends('qty_order_line')
    def _compute_qty_booking(self):
        for record in self:
            qty = record.qty_order_line
            record.qty_booking = qty
    
    @api.onchange('qty_booking')
    def _onchange_qty_available_after_booking(self):
        for record in self:
            record.qty_available_after_booking = record.qty_available - record.qty_booking
