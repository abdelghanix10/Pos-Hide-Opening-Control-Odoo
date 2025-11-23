from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    hide_opening_control = fields.Boolean(
        string='Hide Opening Cash Control',
        help='If enabled, the opening cash control popup will be hidden and automatically set to 0.',
        default=False,
    )