{
    'name': 'POS Hide Opening Control',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Hide opening cash control and set default to 0',
    'description': """
        This module hides the opening cash control popup in the Point of Sale
        and automatically sets the opening cash to 0.
    """,
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets_prod': [
            'pos_hide_opening_control/static/src/app/opening_control_popup_patch.js',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
