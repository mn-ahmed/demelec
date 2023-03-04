from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Payment(models.Model):
    _inherit = 'account.payment'

    exchange_format_id = fields.Many2one(
        comodel_name="exchange.configuration", string="Imprimante", required=False, )
    recipient_name = fields.Char(string="Nom du destinataire")
    donor_name = fields.Char(string="Nom du donateur")
    #due_date = fields.Date(string='Date d\'échéance', required=False)
    location = fields.Char(
        string='', related='company_id.state_id.name', required=False)
    bank = fields.Char(string='Banque', required=False)
    bnk = fields.Char(string='Code Bank', required=False)
    aga = fields.Char(string='Code Agance',  required=False)
    compt = fields.Char(string='Compte',  required=False)
    cle = fields.Char(string='Clé', required=False)
    address = fields.Text(string="Adresse du Donneur",
                          compute="_compute_address")
    bank_address = fields.Text(
        string="Adresse du banque", compute='_compute_bank_address', readonly=False)
    # amount_in_words = fields.Char(
    #     string='Montant en texte', compute='_amount_in_word', required=False)
    #
    # def _amount_in_word(self):
    #     for rec in self:
    #         rec.amount_in_words = str(
    #             rec.currency_id.amount_to_text(rec.amount))

    @api.depends('partner_bank_id', 'partner_bank_id.bank_id')
    def _compute_bank_address(self):
        for rec in self:
            if rec.partner_bank_id:
                res = [
                    rec.partner_bank_id.bank_id.name,
                    rec.partner_bank_id.bank_id.street,
                    rec.partner_bank_id.bank_id.street2,
                    rec.partner_bank_id.bank_id.city,
                    rec.partner_bank_id.bank_id.zip
                ]

                self.bank_address = ', '.join(filter(bool, res))
            else:
                self.bank_address = ''

    # this function will get required fields and concatenate them in address field
    @api.depends('partner_id', 'company_id')
    def _compute_address(self):
        for rec in self:
            if rec.payment_type == 'outbound':
                res = [rec.company_id.street,
                       rec.company_id.street2,
                       rec.company_id.city,
                       rec.company_id.zip]
                self.address = ', '.join(filter(bool, res))
            else:
                res = [rec.partner_id.street,
                       rec.partner_id.street2,
                       rec.partner_id.city,
                       rec.partner_id.zip]
                self.address = ', '.join(filter(bool, res))

    @api.depends('partner_id', 'company_id', 'payment_type')
    def _compute_available_partner_bank_ids(self):
        res = super(Payment, self)._compute_available_partner_bank_ids()
        for pay in self:
            if pay.payment_type == 'inbound' and pay.payment_method_line_id != 'exchange':
                pay.available_partner_bank_ids = pay.partner_id.bank_ids.filtered(
                    lambda x: x.company_id.id in (False, pay.company_id.id))._origin
            elif pay.payment_type == 'inbound' and pay.payment_method_line_id == 'exchange':
                pay.available_partner_bank_ids = pay.journal_id.bank_account_id
            elif pay.payment_type == 'outbound' and pay.payment_method_line_id != 'exchange':
                pay.available_partner_bank_ids = pay.journal_id.bank_account_id
            else:
                pay.available_partner_bank_ids = pay.partner_id.bank_ids.filtered(
                    lambda x: x.company_id.id in (False, pay.company_id.id))._origin
        return res

    @api.onchange('partner_bank_id')
    def _compute_str(self):
        for rec in self:
            if rec.partner_bank_id and rec.partner_bank_id.acc_number:
                rib = rec.partner_bank_id.acc_number
                p = rib.replace(" ", "")
                res = p[-20:]
                rec.bnk = rib[0:2]
                rec.aga = rib[2:5]
                rec.compt = rib[5:18]
                rec.cle = rib[18:20]
                rec.bank = rec.partner_bank_id.bank_id.name

    def print_exchange(self):
        if not self.exchange_format_id:
            raise UserError('No printer model is selected')
        else:
            return self.env.ref('dynamic_print_exchange.action_report_exchange').report_action(self)

    @api.onchange('partner_id', 'payment_type')
    def _onchange_partner(self):
        if self.payment_type == 'outbound':
            self.recipient_name = self.partner_id.name
            self.donor_name = self.company_id.name
        else:
            self.recipient_name = self.company_id.name
            self.donor_name = self.partner_id.name
