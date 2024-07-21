from odoo import models, fields, api, _

class EditInventory(models.Model):
    _inherit = 'stock.picking'

    is_booking = fields.Boolean(string='Booking Order',  store=True)
    sale_id = fields.Many2one(string="Sales Order", compute="_compute_is_booking", readonly=True)

    # booking_id = fields.Many2one('sale.order', string='booking_id')

    
    # @api.depends('is_booking')
    # def _compute_booking_id(self):
    #     for record in self:
    #         record.is_booking = record.booking_id.is_booking

    @api.depends('is_booking','sale_id')
    def _compute_is_booking(self):
        for record in self:
                record.is_booking = self.env['sale.order'].search([('sale_id','=',record.id)]).mapped('is_booking')
               

    
    