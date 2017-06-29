# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
import time


class ProjectTask(models.Model):
	"""docstring for project_task"""
	_inherit = "project.task"

	# days = fields.Selection([('1', '1'),
	# 						('2', '2'),
	# 						('3', '3'),
	# 						('4', '4'),
	# 						('5', '5')
	# 						], 'Days', default='1')
	details = fields.Text('Details')
	catalogue_id = fields.Many2one('service.catalogue', 'Service Catalogue')

class ServiceCatalogue(models.Model):
	_name = "service.catalogue"

	name = fields.Char('Name', required=True, translate=True)
	active = fields.Boolean(default=True)
	role_id = fields.Many2one('service.catalogue.role', 'Role')
	task_ids = fields.One2many('project.task', 'catalogue_id', 'Tasks')
	assing_ids = fields.One2many('service.catalogue.assign', 'catalogue_id', 'Assignation')
	# role_count = fields.Integer('Role Catalogue count', compute='compute_role_count')
	# visibility = fields.Selection([('owner', 'Owner'),
	# 								('follower', 'Follower'),
	# 								('all', 'All')
	# 								], 'Visibility', default='owner')

	# @api.one
	# def compute_role_count(self):
	# 	self.role_count = self.search_count([('role_id','=', self.role_id.id)])

	@api.onchange('role_id')
	def _onchange_service_visibility(self):
		if self.role_id and self.role_id.name == 'Aide comptable':
			self.visibility = 'owner'
		else: 
			self.visibility = 'all'


# class ServiceCatalogueRole(models.Model):
# 	"""docstring for service_catalogue_role"""
# 	_name = "service.catalogue.role"

# 	name = fields.Char('Name', required=True, translate=True)
# 	active = fields.Boolean(default=True)
# 	description = fields.Text('Description')
# 	catalogue_ids = fields.One2many('service.catalogue', 'role_id', 'Service Catalogue')
# 	assign_ids = fields.One2many('service.catalogue.assign', 'role_id', 'Assignation')


class ServiceCatalogueAssign(models.Model):
	"""docstring for service_catalogue_assign"""
	_name = "service.catalogue.assign"

	name = fields.Char('Name', required=True, translate=True)
	active = fields.Boolean(default=True)
	# role_id = fields.Many2one('service.catalogue.role', 'Role')
	catalogue_id = fields.Many2one('service.catalogue', 'Service Catalogue')
	user_id = fields.Many2one('res.users', 'Assign to')

	@api.model
	def _default_date(self):
		current_date = time.strftime(DF)
		return current_date

	date_begin = fields.Date('Begin date', default=_default_date, index=True)