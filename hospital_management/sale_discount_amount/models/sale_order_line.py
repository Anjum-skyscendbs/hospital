from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Monetary('Discount Amount', compute='_calc_discount_amount', store=True)
    # discount_percentage = fields.Float(string='Discount(%)', digits='Discount', default=0.0)

