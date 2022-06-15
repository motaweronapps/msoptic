# -*- coding: utf-8 -*-
# from odoo import http


# class Msoptic(http.Controller):
#     @http.route('/msoptic/msoptic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/msoptic/msoptic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('msoptic.listing', {
#             'root': '/msoptic/msoptic',
#             'objects': http.request.env['msoptic.msoptic'].search([]),
#         })

#     @http.route('/msoptic/msoptic/objects/<model("msoptic.msoptic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('msoptic.object', {
#             'object': obj
#         })
