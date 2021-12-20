# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class informacion(models.Model):
    _name = 'odoo_no_basico.informacion'
    _description = 'exemplo de odoo basico'
    _sql_constraints = [('nome_unico', 'unique(name)', 'Non se pode repetir o nome')]
    _order = "descripcion desc"

    name = fields.Char(string="Titulo!")
    descripcion = fields.Text(string="A Descripcion")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    sexo_traducido = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')], string='Sexo')
    alto_en_cms = fields.Integer(string="Alto en centímetros")
    volume = fields.Float(compute="_volume", store=True)
    longo_en_cms = fields.Integer(string="Longo en centímetros")
    ancho_en_cms = fields.Integer(string="Ancho en centímetros")
    peso = fields.Float()
    densidade = fields.Float()
    literal = fields.Char(store=False)
    peso = fields.Float(digits=(6, 2), string="Peso en Kg.s", default=2.7)
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto")
    adxunto = fields.Binary(string="Arquivo adxunto")
    moeda_id = fields.Many2one('res.currency', domain="[('position','=','after')]")
    gasto_en_moeda_seleccionada_polo_usuario = fields.Monetary("Gasto na moeda seleccionada", "moeda_id")
    moeda_en_texto = fields.Char(related="moeda_id.currency_unit_label",
                                 string="Moeda en formato texto", store=True)
    moeda_euro_id = fields.Many2one('res.currency',
                                    default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],
                                                                                         limit=1))
    creador_da_moeda = fields.Char(related="moeda_id.create_uid.login",
                                    string="Usuario creador da moeda", store=True)
    gasto_en_euros = fields.Monetary("Gasto en Euros", 'moeda_euro_id')
    lineapedido_ids = fields.One2many("odoo_no_basico.lineapedido", 'pedido_id')


    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms)

    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = 100 * (float(rexistro.peso) / float(rexistro.volume))
            else:
                rexistro.densidade = 0

    @api.onchange('alto_en_cms')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
            else:
                rexistro.literal = ""

    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)

    def _cambia_campo_sexo(self, rexistro):
        rexistro.sexo_traducido = "Hombre"
