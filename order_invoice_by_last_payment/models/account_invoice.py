# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management SOlution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

from odoo import models, api, _, fields

from datetime import datetime

class AccountInvoice(models.Model):
    # Se define la clase de python AccountInvoice para poder heredar la existente
    # de odoo, la variable _inherit establece que modelo de odooo será heredado.
    _inherit = "account.invoice"


    last_payment = fields.Char(compute='_get_last_payment_date', store=True)
    # Se define un campo computado, que será establecido mediante la función 
    # _get_last_payment_date. El parámetro store indica que el campo será calculado
    # unicamente cuando se cumpla la condición del decorador @api.depends

    @api.one
    @api.depends('payment_ids')
    def _get_last_payment_date(self):
        for invoice in self: # el campo payment_ids es original de odoo y almacena los pagos de la factura
            #datetime.strptime(pay.payment_date, lang.date_format).strftime(DEFAULT_SERVER_DATE_FORMAT)
            payment_list = [pay.payment_date.strftime('%d/%m/%Y') for pay in invoice.payment_ids]
            # La función sorted ordenara los registros mediante un campo el cual se indica mediante el
            # parámetro key, el parámetro reverse indica que el orden será de mayor a menor.
            invoice.last_payment = ', '.join(payment_list) # una vez ordenados los pagos podremos tomar el
            # primero de todos y asignaremos la fecha.

