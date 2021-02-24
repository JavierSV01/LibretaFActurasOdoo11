from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'libretafacturas.cliente'
    cod = fields.Char('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    edad = fields.Integer('Edad', required=True)
    facturas = fields.Many2many('libretafacturas.facturas')

    @api.one
    def limpiar(self):
        self.cod = ""
        self.nombre = ""
        self.edad = ""
        return True