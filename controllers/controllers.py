# -*- coding: utf-8 -*-
from openerp import http

# class ProductVarianTax(http.Controller):
#     @http.route('/product_varian_tax/product_varian_tax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_varian_tax/product_varian_tax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_varian_tax.listing', {
#             'root': '/product_varian_tax/product_varian_tax',
#             'objects': http.request.env['product_varian_tax.product_varian_tax'].search([]),
#         })

#     @http.route('/product_varian_tax/product_varian_tax/objects/<model("product_varian_tax.product_varian_tax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_varian_tax.object', {
#             'object': obj
#         })