from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Monetary('Discount Amount', compute='_calc_discount_amount', store=True)
    @api.depends('price_unit', 'discount')
    def _calc_discount_amount(self):
        # Exercise-6 Q-10
        for order in self:
            order.discount_amount = (order.price_unit * order.discount) / 100
