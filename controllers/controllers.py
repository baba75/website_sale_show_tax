# -*- coding: utf-8 -*-
from odoo import http

# class /users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduliEcobeton/12.0/websiteSaleShowTax(http.Controller):
#     @http.route('//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax.listing', {
#             'root': '//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax',
#             'objects': http.request.env['/users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax./users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax'].search([]),
#         })

#     @http.route('//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax//users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax/objects/<model("/users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax./users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax.object', {
#             'object': obj
#         })