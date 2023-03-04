# -*- coding: utf-8 -*-
# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class TimbreFiscal(models.Model):
    _inherit = 'account.move'

    in_words = fields.Char(string='amount in words', compute='_compute_amount_in_words')
    tva = fields.Monetary(string='TVA', compute='_compute_taxes', store=True, readonly=True,)
    timbre = fields.Monetary(string='Timbre fiscal', compute='_compute_taxes',  store=True, readonly=True,)

    @api.depends('amount_tax', 'invoice_line_ids', 'move_type')
    def _compute_taxes(self):
        for invoice in self:
            tva = invoice.amount_tax
            timbre = 0.00
            tmb = self.env['account.tax'].search([('tax_group_id.name', '=', 'Timbre Fiscal')], limit=1)
            for tf in invoice.invoice_line_ids:
                if tf.product_id.timbre_fiscal:
                    timbre = timbre + tmb.amount
                    tva = tva - timbre
                else:
                    tva = tva
                    timbre = 0.0
            invoice.timbre = timbre
            invoice.tva = tva



    def _compute_amount_in_words(self):
        for record in self:
            record.in_words = str(record.currency_id.amount_to_text(record.amount_total))
