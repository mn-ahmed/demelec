# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def _default_outbound_payment_methods(self):
        res = super()._default_outbound_payment_methods()
        if self.type == 'bank':
            res |= self.env.ref('dynamic_print_exchange.account_payment_method_exchange_outbound')
        return res

    def _default_inbound_payment_methods(self):
        res = super()._default_inbound_payment_methods()
        if self.type == 'bank':
            res |= self.env.ref('dynamic_print_exchange.account_payment_method_exchange_inbound')
        return res
