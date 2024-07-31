{
    'name': 'Shopee Integration v1',
    'version': '0.1.2',
    'depends': [
        'base',
        'base_import',
        'product',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/shopee_integration_views.xml',
        'views/shopee_integration_menus.xml',
    ],
    'application': True
}