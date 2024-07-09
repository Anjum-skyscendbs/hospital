from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    discount_amount = fields.Float('Discount Amount', store=True)

    # @api.onchange('price_unit', 'discount')
    # def onchange_gender(self):
    #     # E-6 Q-11
    #     for line in self:
    #         line.discount_amount = (line.price_unit * line.discount) / 100

    @api.depends('price_unit', 'quantity', 'discount')
    def _compute_discount_amount(self):
        for line in self:
            line.discount_amount = (line.price_unit * line.quantity * line.discount) / 100

    @api.onchange('discount')
    def _onchange_discount(self):
        if self.discount:
            self.discount_amount = (self.price_unit * self.quantity * self.discount) / 100
