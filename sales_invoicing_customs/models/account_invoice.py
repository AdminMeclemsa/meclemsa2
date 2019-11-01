# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management SOlution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

from odoo import models, api, _, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state")
    zip = fields.Char()
    country_id = fields.Many2one("res.country")
    street_name = fields.Char()
    street_number = fields.Char()
    street_number2 = fields.Char()
    l10n_mx_edi_locality = fields.Char()
    terms_txt = fields.Html()

    @api.multi
    @api.onchange("partner_id")
    def changes_address_data(self):
        for invoice in self:
            invoice.street2 = invoice.partner_id.street2
            invoice.city = invoice.partner_id.city
            invoice.state_id = invoice.partner_id.state_id
            invoice.zip = invoice.partner_id.zip
            invoice.country_id = invoice.partner_id.country_id
            invoice.street_name = invoice.partner_id.street_name
            invoice.street_number = invoice.partner_id.street_number
            invoice.street_number2 = invoice.partner_id.street_number2
            invoice.l10n_mx_edi_locality = invoice.partner_id.l10n_mx_edi_locality
    
    def write(self, values):
        partner_vals = {}
        if values.get("street2"):
            partner_vals["street2"] = values.get("street2")
        if values.get("city"):
            partner_vals["city"] = values.get("city")
        if values.get("state_id"):
            partner_vals["state_id"] = values.get("state_id")
        if values.get("zip"):
            partner_vals["zip"] = values.get("zip")
        if values.get("country_id"):
            partner_vals["country_id"] = values.get("country_id")
        if values.get("street_name"):
            partner_vals["street_name"] = values.get("street_name")
        if values.get("street_number"):
            partner_vals["street_number"] = values.get("street_number")
        if values.get("street_number2"):
            partner_vals["street_number2"] = values.get("street_number2")
        if values.get("l10n_mx_edi_locality"):
            partner_vals["l10n_mx_edi_locality"] = values.get("l10n_mx_edi_locality")
        if partner_vals:
            if not values.get("partner_id"):
                self.partner_id.write(partner_vals)
        return super(AccountInvoice, self).write(values)

