# -*- coding: utf-8 -*-
# from odoo import http


# class OdooNoBasico(http.Controller):
#     @http.route('/odoo_no_basico/odoo_no_basico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_no_basico/odoo_no_basico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_no_basico.listing', {
#             'root': '/odoo_no_basico/odoo_no_basico',
#             'objects': http.request.env['odoo_no_basico.odoo_no_basico'].search([]),
#         })

#     @http.route('/odoo_no_basico/odoo_no_basico/objects/<model("odoo_no_basico.odoo_no_basico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_no_basico.object', {
#             'object': obj
#         })
