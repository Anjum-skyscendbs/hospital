from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Monetary('Discount Amount', compute='_calc_discount_amount', store=True)
    discount_per = fields.Float(string='Discount(%)', digits='Discount', default=0.0)

    # @api.depends('price_unit', 'discount')
    # def _calc_discount_amount(self):
    #     for order in self:
    #         order.discount_amount = (order.price_unit * order.discount) / 100

    # Exercise-6 Q-10 The above mentioned discount amount field must change when you add a
    # percentage in the discount percentage in the sale order line.
    @api.depends('price_unit', 'product_uom_qty', 'discount_per')
    def _calc_discount_amount(self):
        for order in self:
            order.discount_amount = (order.price_unit * order.product_uom_qty) * (order.discount_per / 100)
    @api.onchange('discount_per', 'price_unit', 'product_uom_qty')
    def _onchange_discount_per(self):
        # 140 * 1 quantity * 4 discount / 100
        # 140 * 0.04 = 5.60 Total discount amount ans is 5.60
        if self.discount_per:
            self.discount_amount = (self.price_unit * self.product_uom_qty) * (self.discount_per / 100)
        else:
            self.discount_amount = 0.0

