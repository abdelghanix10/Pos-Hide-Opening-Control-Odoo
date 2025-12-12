/** @odoo-module */

import { OpeningControlPopup } from "@point_of_sale/app/components/popups/opening_control_popup/opening_control_popup";
import { patch } from "@web/core/utils/patch";
import { onMounted } from "@odoo/owl";

patch(OpeningControlPopup.prototype, {
  setup() {
    super.setup();
    if (this.pos.config.hide_opening_control) {
      onMounted(() => {
        this.state.notes = "";
        this.state.openingCash =
          this.pos.config.default_opening_cash.toString();
        this.confirm();
      });
    }
  },
});
