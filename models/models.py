# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class /users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax(models.Model):
#     _name = '/users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax./users/baba/nuvola.ecobeton.it/amministrazione/odoo/moduli_ecobeton/12.0/website_sale_show_tax'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100