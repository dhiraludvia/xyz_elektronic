from odoo import models, fields, api


class InventoryBookingPivot(models.Model):
    _name = 'inventory.booking.pivot'
    _auto = False
    
    partner_id = fields.Many2one('res.partner', 'Customer')
    date_order = fields.Datetime('Order Date')
    amount_total = fields.Float('Total Amount')

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW inventory_booking_pivot AS (
                SELECT
                    so.id,
                    so.partner_id,
                    so.date_order,
                    so.amount_total
                FROM
                    sale_order so
                WHERE
                    so.is_booking = TRUE
            )
        """)
