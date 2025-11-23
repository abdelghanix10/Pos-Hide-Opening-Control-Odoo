from odoo import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def open_frontend_cb(self):
        """Override to automatically set opening cash to the default amount if in opening_control state."""
        for session in self:
            if session.state == 'opening_control' and session.config_id.cash_control and session.config_id.hide_opening_control:
                session.set_cashbox_pos(session.config_id.default_opening_cash, None)
        return super().open_frontend_cb()
