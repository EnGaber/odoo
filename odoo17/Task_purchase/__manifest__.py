{
    'name': 'Purchase_Task',
    'version': '1.0',
    'category': 'Purchase Orders',
    'complexity': 'easy',
    'description': "Manage Purchase Requests",
    'depends': [
        'base',
        'purchase',
        'purchase_stock',
        'mail',
        'sale',
        'sale_stock',
        'portal',
        'utm'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/purchase_request_reject_wizard.xml',
        'views/purchase_requests.xml',
        'data/email_templates.xml',
        'data/sequence_data.xml',
        'views/purchase_order.xml',
        'views/stock_picking.xml',
        'views/sale_order.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}