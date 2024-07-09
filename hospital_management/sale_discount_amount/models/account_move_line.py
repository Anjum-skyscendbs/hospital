from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    discount_amount = fields.Float('Discount Amount', store=True)

    @api.onchange('price_unit', 'discount')
    def onchange_gender(self):
        # E-6 Q-11
        for line in self:
            line.discount_amount = (line.price_unit * line.discount) / 100

    # E-6 Q-12
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('discount', 0):
                vals.update({
                    'discount_amount': vals['price_unit'] * vals['discount'] / 100.0
                })
        return super(AccountMoveLine, self).create(vals_list)

    # E-6 Q-12
    def write(self, vals):
        for line in self:
            if vals.get('discount', 0):
                price_unit = vals.get('price_unit') and vals['price_unit'] or line.price_unit
                vals.update({
                    'discount_amount': price_unit * vals['discount'] / 100.0
                })
        return super().write(vals)
