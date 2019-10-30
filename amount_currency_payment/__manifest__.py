# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management SOlution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

# Archivo básico que funciona para definir las propiedades de un modulo de odoo
{
    'name': 'Show amount of payments with currency company',
    'author': '@Neto_odoo',
    'category': 'Accounting',
    'sequence': 50,
    'summary': 'Show amount of payments with currency company',
    'version': '1.0',
    'description': "",
    'depends': [
        'account', # Lista de modulos de los que depende este modulo
    ],
    'data': [
        'views/account_payment_views.xml'# Todos lo archivos xml, csv deben ser cargados en esta sección
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}
