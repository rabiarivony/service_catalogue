# -*- coding: utf-8 -*-
from odoo import http

# class ServiceCatalogue(http.Controller):
#     @http.route('/service_catalogue/service_catalogue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/service_catalogue/service_catalogue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('service_catalogue.listing', {
#             'root': '/service_catalogue/service_catalogue',
#             'objects': http.request.env['service_catalogue.service_catalogue'].search([]),
#         })

#     @http.route('/service_catalogue/service_catalogue/objects/<model("service_catalogue.service_catalogue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('service_catalogue.object', {
#             'object': obj
#         })