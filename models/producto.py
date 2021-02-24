#-*- coding: utf-8 -*-
from odoo import models, fields, api

class Producto(models.Model):
    _name = 'libretafacturas.producto'
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    precio = fields.Integer('Precio', required=True)


