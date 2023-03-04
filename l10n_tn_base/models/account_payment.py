# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Payment(models.Model):
    _inherit = 'account.payment'

    cr_date = fields.Date(string='Date', default=fields.Date.today, required=False)
    amount_in_words = fields.Char(string='Montant en texte', compute='_amount_in_word', required=False)

    def _amount_in_word(self):
        for rec in self:
            rec.amount_in_words = str(rec.currency_id.amount_to_text(rec.amount))