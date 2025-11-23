{
    'name': 'POS Hide Opening Control',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Add option to hide opening cash control popup and set default to 0',
    'description': """
        This module adds an option to hide the opening cash control popup in the Point of Sale
        and automatically sets the opening cash to 0 when enabled.
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale.assets_prod': [
            'pos_hide_opening_control/static/src/app/opening_control_popup_patch.js',
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}
