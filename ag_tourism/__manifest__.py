{
    'name': 'Tourism Agency',

    'category': 'Hidden',
    'version': '14.0.0.0',
    'depends': [
        'base', 'account'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/booking.xml',
        'wizards/register_payment.xml'
    ],
    'auto_install': True,

}