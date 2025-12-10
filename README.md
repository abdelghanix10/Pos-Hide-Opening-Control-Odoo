# POS Hide Opening Control

This Odoo module allows you to streamline the Point of Sale session opening process by hiding the opening cash control popup and automatically setting a default opening cash amount.

## Features

- **Hide Opening Control Popup**: Option to skip the manual cash counting step when opening a POS session.
- **Configurable Default Amount**: Set a specific default opening cash amount (e.g., 0 or a fixed float fund) that will be automatically applied.
- **Per-POS Configuration**: Configure these settings individually for each Point of Sale.

## Configuration

1. Go to **Point of Sale** > **Configuration** > **Settings**.
2. Select the Point of Sale you want to configure.
3. Locate the **Hide Opening Cash Control** setting (typically found near the IoT Box or Hardware settings).
4. Enable the checkbox.
5. Enter the desired amount in the **Default Opening Cash** field that appears.
6. Save the settings.

## Usage

1. Open a new session for the configured Point of Sale.
2. The Opening Cash Control popup will be automatically handled.
3. The session will open with the configured opening cash amount set.

## Technical Details

- **Odoo Version**: 18.0
- **Dependencies**: `point_of_sale`
- **License**: LGPL-3

## Installation

1. Clone this repository into your Odoo addons directory.
2. Update the app list in Odoo.
3. Install the "POS Hide Opening Control" module.
