from num2words import num2words
from odoo import api, fields, models


class ChequeConfiguration(models.Model):
    _name = 'cheque.configuration'
    _rec_name = 'name'
    _description = 'Cheque Configuration'

    name = fields.Char(string='Format Cheque', )

    cheque_img = fields.Binary(string="Cheque Image", )
    font_size = fields.Integer(string="Font Size", default=20)

    date_margin_top = fields.Integer(string="Margin Top", default=250)
    date_margin_left = fields.Integer(string="Margin Left", default=420)

    recipient_margin_top = fields.Integer(string="Margin Top", default=125)
    recipient_margin_left = fields.Integer(string="Margin Left", default=290)

    amount_margin_top = fields.Integer(string="Margin Top", default=18)
    amount_margin_left = fields.Integer(string="Margin Left", default=700)

    text_amount_1_margin_top = fields.Integer(string="Margin Top", default=65)
    text_amount_1_margin_left = fields.Integer(string="Margin Left", default=290)

    text_amount_2_margin_top = fields.Integer(string="Margin Top", default=95)
    text_amount_2_margin_left = fields.Integer(string="Margin Left", default=177)

    acc_pay_margin_top = fields.Float('Pay From Top', default=18)
    acc_pay_margin_left = fields.Float('Pay From Left', default=150)

    def get_html_date(self, date):
        return """ 
            <div style="top:{}px;left:{}px;position:absolute;">
                {}
            </div>
            """.format(self.date_margin_top, self.date_margin_left, date)

    def get_html_recipient(self, recipient):
        return """ 
            <div style="top:{}px;left:{}px;position:absolute;">
                {}
            </div>
            """.format(self.recipient_margin_top, self.recipient_margin_left, recipient)

    def get_html_amount(self, amount):
        return """ 
            <div style="top:{}px;left:{}px;position:absolute;">
                {}
            </div>
            """.format(self.amount_margin_top, self.amount_margin_left, amount)

    def get_html_text_amount_1(self, text_amount):
        return """ 
            <div style="top:{}px;left:{}px;position:absolute;">
                {}
            </div>
            """.format(self.text_amount_1_margin_top, self.text_amount_1_margin_left, text_amount)

    def get_html_text_amount_2(self, text_amount):
        return """ 
            <div style="top:{}px;left:{}px;position:absolute;">
                {}
            </div>
            """.format(self.text_amount_2_margin_top, self.text_amount_2_margin_left, text_amount)

    def get_html_style(self):
        return """
            <style>
                div {
                      font-size: %spx;
                    }
            </style>
            """ % self.font_size
