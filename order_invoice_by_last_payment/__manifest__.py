# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management Solution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

#Archivo básico, cualquier módulo de odoo debe llevar el archivo __manifest__.py y el __init__.py
{
    'name': 'Order invoices by payments',
    'author': '@Neto_odoo',
    'category': 'Accounting',
    'sequence': 50,
    'summary': 'Order invoices by payments',
    'version': '1.0',
    'description': "",
    'depends': [
        'account', 
    ],
    'data': [
        'views/account_invoice_views.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}
