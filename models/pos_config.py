from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    hide_opening_control = fields.Boolean(
        string='Hide Opening Cash Control',
        help='If enabled, the opening cash control popup will be hidden and automatically set to the default amount.',
        default=False,
    )
    default_opening_cash = fields.Float(
        string='Default Opening Cash',
        help='The default opening cash amount to set when hiding the opening control popup.',
        default=0.0,
    )