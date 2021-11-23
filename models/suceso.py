from odoo import models, fields, api


class suceso(models.Model):
    _name = 'odoo_no_basico.suceso'
    _description = 'exemplo de odoo basico'

    name = fields.Char(required=True, size=20, string="Suceso")
    descripcion = fields.Text(string="A Descripción do Suceso")  # string é a etiqueta do campo
    nivel = fields.Selection([('Baixo', 'Baixo'), ('Medio', 'Medio'), ('Alto', 'Alto')], string='Nivel')
    data_hora = fields.Datetime(string="Data e Hora", default=lambda self: fields.Datetime.now())