from odoo import fields, models


class attraction(models.Model):
    _name = 'attraction'
    _description = 'attraction'

    name = fields.Char("Name")
    limit = fields.Integer("Limit")
