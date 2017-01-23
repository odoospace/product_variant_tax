# -*- coding: utf-8 -*-

from openerp import models, fields, api

class product_prodcut(models.Model):
    _inherit = 'product.product'

    taxes_id = fields.Many2many('account.tax', 'product_prodcut_taxes_rel', 'prod_id', 'tax_id', string='Customer Taxes',
        domain=[('type_tax_use', '=', 'sale')])
