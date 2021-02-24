#-*- coding: utf-8 -*-
from odoo import models, fields, api

class Facturas(models.Model):
    _name = 'libretafacturas.facturas'
    cod = fields.Integer('Codigo factura', required=True)
    productos = fields.Many2many('libretafacturas.producto')


        	
    