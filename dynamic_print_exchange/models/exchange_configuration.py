# from num2words import num2words
from odoo import api, fields, models


class ExchangeConfiguration(models.Model):
    _name = 'exchange.configuration'
    _rec_name = 'name'
    _description = 'Exchange Configuration'

    name = fields.Char(string='Printer', )

    printer_img = fields.Binary(string="Image de l\'imprimante", )
    font_size = fields.Float(string="Font Size", default=20)

    # ----------------------- Line 1 ----------------------------
    location_1_top = fields.Float(string="Local Margin Top", default=240)
    location_1_left = fields.Float(string="Local Margin Left", default=390)

    date_1_top = fields.Float(string="Date Margin Top", default=250)
    date_1_left = fields.Float(string="Date Margin Left", default=390)

    due_date_1_top = fields.Float(string="Due date Margin Top", default=150)
    due_date_1_left = fields.Float(string="Due date Margin Left", default=290)

    # -----------------------Line 2 -----------------------------
    rib_top = fields.Float(string="Margin Top", default=150)
    rib_left = fields.Float(string="Margin Left", default=290)

    bnk_1_top = fields.Float(string="Bank Margin Top", default=150)
    bnk_1_left = fields.Float(string="Bank Margin Left", default=290)

    aga_1_top = fields.Float(string="Agency Margin Top", default=150)
    aga_1_left = fields.Float(string="Agency Margin Left", default=290)

    compt_1_top = fields.Float(string="Account Margin Top", default=150)
    compt_1_left = fields.Float(string="Account Margin Left", default=290)

    cle_1_top = fields.Float(string="Key Margin Top", default=150)
    cle_1_left = fields.Float(string="Key Margin Left", default=290)

    amount_1_top = fields.Float(string="Amount Margin Top", default=26)
    amount_1_left = fields.Float(string="Amount Margin Left", default=700)

    # ------------------------ Line 3 --------------------------------
    recipient_top = fields.Float(string="Recipient Margin Top", default=125)
    recipient_left = fields.Float(string="Recipient Margin Left", default=290)

    amount_2_top = fields.Float(string="Amount Margin Top", default=26)
    amount_2_left = fields.Float(string="Amount Margin Left", default=700)

    # ----------------------- Line 4 ----------------------------------
    text_amount_top = fields.Float(string="Text Margin Top", default=95)
    text_amount_left = fields.Float(string="Text Margin Left", default=177)

    # ------------------------ line 5 --------------------------------
    location_top = fields.Float(string="Local Margin Top", default=26)
    location_left = fields.Float(string="Local Margin Left", default=700)

    date_2_top = fields.Float(string="Date Margin Top", default=250)
    date_2_left = fields.Float(string="Date Margin Left", default=390)

    due_date_2_top = fields.Float(string="Due date Margin Top", default=150)
    due_date_2_left = fields.Float(string="Due date Margin Left", default=290)

    # ------------------------ line 6 --------------------------------
    bnk_2_top = fields.Float(string="Bank Margin Top", default=150)
    bnk_2_left = fields.Float(string="Bank Margin Left", default=290)

    aga_2_top = fields.Float(string="Agency Margin Top", default=150)
    aga_2_left = fields.Float(string="Agency Margin Left", default=290)

    compt_2_top = fields.Float(string="Account Margin Top", default=150)
    compt_2_left = fields.Float(string="Account Margin Left", default=290)

    cle_2_top = fields.Float(string="Key Margin Top", default=150)
    cle_2_left = fields.Float(string="Key Margin Left", default=290)

    bank_top = fields.Float(string="Bank Margin Top", default=150)
    bank_left = fields.Float(string="Bank Margin Left", default=290)

    # ------------------------- line 7 - 8 ------------------------------
    payed_top = fields.Float(string="Payer Margin Top", default=150)
    payed_left = fields.Float(string="Payer Margin Left", default=290)

    payed_address_top = fields.Float(string="Address Margin Top", default=370)
    payed_address_left = fields.Float(string="Address Margin Left", default=410)