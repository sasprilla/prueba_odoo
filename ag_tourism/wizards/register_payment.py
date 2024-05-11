from odoo import fields, models, _


class RegisterPaymentWizard(models.TransientModel):
    _name = 'register.payment.wizard'
    _description = 'register payment wizard'

    payment_method = fields.Selection([('cash', _('Cash')),
                                       ('transfer', _('Transfer')),
                                       ('card', _('Card'))], "payment method")
    amount = fields.Float("Amount")
    booking_id = fields.Many2one( "booking")

    def action_register(self):
        self.booking_id.write({
            'state': 'reserved',
            'payment_method': self.payment_method,
            'initial_amount': self.amount
        })
