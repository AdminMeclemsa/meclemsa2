# -*-encoding: utf-8 -*-
#
# module written to Odoo,Open Source Management SOlution
#
#Developer(s): Luis Ernesto García Medina
#              (ernesto.r.2.em@gmail.com)

from odoo import models, api, _, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    terms_template_id = fields.Many2one('mail.template', string='Email Template',
                                  domain="[('model','=','sale.order')]",
                                  #default=lambda self: self.env.ref('sales_invoicing_customs.email_template_sale_terms'),
                                  required=False)
    terms_txt = fields.Html(compute="_get_html_content")

    @api.multi
    @api.depends("terms_template_id")
    def _get_html_content(self):
        for sale in self:
            if sale.id and sale.terms_template_id:
                template = sale.terms_template_id.with_context(lang=self.env.user.lang)
                sale.terms_txt = template._render_template(template.body_html, template.model_id.model, sale.id or 0)

    l10n_mx_edi_payment_method_id = fields.Many2one('l10n_mx_edi.payment.method',
        string='Payment Way',
        readonly=True,
        states={'draft': [('readonly', False)]},
        help='Indicates the way the invoice was/will be paid, where the '
        'options could be: Cash, Nominal Check, Credit Card, etc. Leave empty '
        'if unkown and the XML will show "Unidentified".',
        default=lambda self: self.env.ref('l10n_mx_edi.payment_method_otros',
                                          raise_if_not_found=False))
    l10n_mx_edi_usage = fields.Selection([
        ('G01', 'Acquisition of merchandise'),
        ('G02', 'Returns, discounts or bonuses'),
        ('G03', 'General expenses'),
        ('I01', 'Constructions'),
        ('I02', 'Office furniture and equipment investment'),
        ('I03', 'Transportation equipment'),
        ('I04', 'Computer equipment and accessories'),
        ('I05', 'Dices, dies, molds, matrices and tooling'),
        ('I06', 'Telephone communications'),
        ('I07', 'Satellite communications'),
        ('I08', 'Other machinery and equipment'),
        ('D01', 'Medical, dental and hospital expenses.'),
        ('D02', 'Medical expenses for disability'),
        ('D03', 'Funeral expenses'),
        ('D04', 'Donations'),
        ('D05', 'Real interest effectively paid for mortgage loans (room house)'),
        ('D06', 'Voluntary contributions to SAR'),
        ('D07', 'Medical insurance premiums'),
        ('D08', 'Mandatory School Transportation Expenses'),
        ('D09', 'Deposits in savings accounts, premiums based on pension plans.'),
        ('D10', 'Payments for educational services (Colegiatura)'),
        ('P01', 'To define'),
    ], 'Usage', default='P01',
        help='Used in CFDI 3.3 to express the key to the usage that will '
        'gives the receiver to this invoice. This value is defined by the '
        'customer. \nNote: It is not cause for cancellation if the key set is '
        'not the usage that will give the receiver of the document.')

    @api.multi
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update(
            {'l10n_mx_edi_payment_method_id': self.l10n_mx_edi_payment_method_id.id,
             'l10n_mx_edi_usage': self.l10n_mx_edi_usage,
             'street2' : self.partner_id.street2,
             'city' : self.partner_id.city,
             'state_id' : self.partner_id.state_id and self.partner_id.state_id.id,
             'zip' : self.partner_id.zip,
             'country_id' : self.partner_id.country_id and self.partner_id.country_id.id,
             'street_name' : self.partner_id.street_name,
             'street_number' : self.partner_id.street_number,
             'street_number2' : self.partner_id.street_number2,
             'l10n_mx_edi_locality' : self.partner_id.l10n_mx_edi_locality,
             })
        return invoice_vals

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    l10n_mx_edi_code_sat_id = fields.Many2one(
        'l10n_mx_edi.product.sat.code',
        related="product_id.l10n_mx_edi_code_sat_id")
