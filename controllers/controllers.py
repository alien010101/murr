# -*- coding: utf-8 -*-
from odoo import http

# class InventarioExpandido(http.Controller):
#     @http.route('/inventario_expandido/inventario_expandido/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario_expandido/inventario_expandido/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario_expandido.listing', {
#             'root': '/inventario_expandido/inventario_expandido',
#             'objects': http.request.env['inventario_expandido.inventario_expandido'].search([]),
#         })

#     @http.route('/inventario_expandido/inventario_expandido/objects/<model("inventario_expandido.inventario_expandido"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario_expandido.object', {
#             'object': obj
#         })