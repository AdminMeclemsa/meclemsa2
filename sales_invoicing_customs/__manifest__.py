# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management Solution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

{
    'name': 'Module with customs devs for meclemsa',
    'author': '@Neto_odoo',
    'category': 'Accounting',
    'sequence': 50,
    'summary': 'Module with customs devs for meclemsa',
    'version': '1.0',
    'description': "",
    'depends': [
        'account',
        'base_address_extended',
        'sale_management',
        'l10n_mx_edi'
    ],
    'data': [
        'data/terms_template.xml',
        'views/account_invoice_views.xml',
        'views/sale_order_view.xml',
        'report/inherit_sale_report.xml'
        
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}
