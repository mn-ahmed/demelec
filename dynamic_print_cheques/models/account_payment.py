from odoo import api, fields, models


class Payment(models.Model):
    _inherit = 'account.payment'

    cheque_format_id = fields.Many2one(comodel_name="cheque.configuration", string="Cheque Format", required=False, )
    recipient_name = fields.Char(string="Recipient Name")
    is_acc_pay = fields.Boolean('Print A/C Payee', default=False)
    # amount_in_words = fields.Char(string='Montant en texte', compute='_amount_in_word', required=False)
    amount_in_words_1 = fields.Char('Amount in word part 1', compute='_split_amount_in_words', required=False)
    amount_in_words_2 = fields.Char('Amount in word part 2', compute='_split_amount_in_words', required=False)

    # def _amount_in_word(self):
    #     for rec in self:
    #         rec.amount_in_words = rec.currency_id.amount_to_text(rec.amount)

    @api.depends('check_amount_in_words')
    def _split_amount_in_words(self):
        self.ensure_one()
        for rec in self:
            words = rec.check_amount_in_words
            txt = str(words).split()
            if len(txt) <= 4:
                words_1 = words
                words_2 = ''
            else:
                words_1 = ' '.join(txt[:4])
                words_2 = ' '.join(txt[4:])
            rec.amount_in_words_1 = words_1
            rec.amount_in_words_2 = words_2

    def print_checks(self):

        return self.env.ref('dynamic_print_cheques.report_cheque').report_action(self)

    @api.onchange('partner_id')
    def _onchange_partner(self):
        self.recipient_name = self.partner_id.name
