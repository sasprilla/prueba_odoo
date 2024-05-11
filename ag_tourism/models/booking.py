from odoo import fields, models, _


class booking(models.Model):
    _name = 'booking'
    _description = 'booking'

    partner_id = fields.Many2one("Partner", "res.partner")
    user_id = fields.Many2one("adviser", "res.users" )
    start_date = fields.Datetime("start date")
    end_date = fields.Datetime("end date")
    attraction_id = fields.Many2one("attraction", "attraction")
    num_passengers = fields.Integer("number of passengers")

    payment_method = fields.Selection([('cash', _('Cash')),
                                       ('transfer', _('Transfer')),
                                       ('card', _('Card'))], "payment method",
                                       default="cash")

    mode_transportation = fields.Selection([('vehicle', _('vehicle')),
                                            ('motorcycle', _('Motorcycle')),
                                            ('public', _('public'))],
                                            "mode of transportation",
                                            default="vehicle")

    state = fields.Selection([('available', _('Available')),
                              ('reserved', _('Reserved'))],
                              "state", default='available')
    initial_amount = fields.Float("Amount")

    def action_register_payment(self):
        wizard_id = self.env['register.payment.wizard'].create({
            'booking_id': self.id
        })
        view_id = self.env.ref('ag_tourism.register_payment_wizard_view').id

        return{
            'type': 'ir.actions.act_window',
            'name': _('Register.payment'),
            'view_mode': 'form',
            'res_model': 'register.payment.wizard',
            'target': 'new',
            'res_id': wizard_id.id,
            'views': [[view_id, 'form']],
        }

    def action_create_invoice(self):

        