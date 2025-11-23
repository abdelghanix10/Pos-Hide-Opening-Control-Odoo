from odoo import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def open_frontend_cb(self):
        """Override to automatically set opening cash to 0 if in opening_control state."""
        for session in self:
            if session.state == 'opening_control' and session.config_id.cash_control:
                session.set_cashbox_pos(0, None)
        return super().open_frontend_cb()
