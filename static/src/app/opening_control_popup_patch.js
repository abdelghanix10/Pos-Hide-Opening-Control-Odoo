/** @odoo-module */

import { OpeningControlPopup } from "@point_of_sale/app/store/opening_control_popup/opening_control_popup";
import { patch } from "@web/core/utils/patch";
import { onMounted } from "@odoo/owl";

patch(OpeningControlPopup.prototype, {
  setup() {
    super.setup();
    onMounted(() => {
      this.state.notes = "";
      this.state.openingCash = "0";
      this.confirm();
    });
  },
});
