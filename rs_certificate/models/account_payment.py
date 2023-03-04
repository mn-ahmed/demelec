# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class AccountPayment(models.Model):
    _inherit = "account.payment"

    signature = fields.Binary(string='Signature')
    total = fields.Monetary(currency_field='currency_id')
    net = fields.Monetary(currency_field='currency_id')
    rate = fields.Float(related='journal_id.rate', string='RS%', required=False)

    @api.onchange('total')
    def amount_onchange(self):
        for rec in self:
            rec.rate == 0.0
            rec.total == 0.0
            rec.net == 0.0
            if not rec.rate and not rec.total:
                rec.amount = rec.amount
            else:
                rec.amount = (rec.rate * rec.total)/100
                rec.net = rec.total - rec.amount

    def rs_print(self):
        return self.env.ref('rs_certificate.action_rs_print_report').report_action(self)