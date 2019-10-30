# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management SOlution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

from odoo import models, api, _, fields

class AccountPayment(models.Model):
    # Se define la clase de python AccountPayment para poder heredar la existente
    # de odoo, la variable _inherit establece que modelo de odooo será heredado.
    _inherit = "account.payment"

    # Definimos el nuevo campo que se calculara en base a la moneda de la compañía.
    # La variable será el campo y como lo encontraremos en la base de datos, en este
    # caso es "amount_currency", la variable fields es importada desde el paquete odoo,
    # El tipo de campo dependerá de la intención del dato a almacenar y el parámetro 
    # compute es utilizado para indicar que el valor de este campo será computado en base a la
    # función definida "_compute_amount_currency"

    amount_currency = fields.Float(compute='_compute_amount_currency')

    @api.multi
    def _compute_amount_currency(self):
        for payment in self:
            company_currency_id = payment.company_id.currency_id
            if company_currency_id:
                payment.amount_currency = payment.currency_id.with_context(date=payment.payment_date).compute(payment.amount,company_currency_id)
            else:
                payment.amount_currency = payment.amount
