# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
import time


class ProjectTask(models.Model):
	"""docstring for project_task"""
	_inherit = "project.task"

	details = fields.Text('Details')
	catalogue_id = fields.Many2one('service.catalogue', 'Service Catalogue')
	assign_id = fields.Many2one('service.catalogue.assign', 'Assignation')


class ServiceCatalogue(models.Model):
	_name = "service.catalogue"

	name = fields.Char('Name', required=True, translate=True)
	active = fields.Boolean(default=True)
	role_id = fields.Many2one('service.catalogue.role', 'Role')
	task_ids = fields.One2many('project.task', 'catalogue_id', 'Tasks')
	assing_ids = fields.One2many('service.catalogue.assign', 'catalogue_id', 'Assignation')

	# @api.one
	# def compute_role_count(self):
	# 	self.role_count = self.search_count([('role_id','=', self.role_id.id)])

	@api.onchange('role_id')
	def _onchange_service_visibility(self):
		if self.role_id and self.role_id.name == 'Aide comptable':
			self.visibility = 'owner'
		else: 
			self.visibility = 'all'


class ServiceCatalogueAssign(models.Model):
	"""docstring for service_catalogue_assign"""
	_name = "service.catalogue.assign"

	name = fields.Char('Name', required=True, translate=True)
	active = fields.Boolean(default=True)
	# role_id = fields.Many2one('service.catalogue.role', 'Role')
	catalogue_id = fields.Many2one('service.catalogue', 'Service Catalogue')
	user_id = fields.Many2one('res.users', 'Assign to')
	task_ids = fields.One2many('project.task', 'catalogue_id', 'Tasks')

	@api.model
	def _default_date(self):
		current_date = time.strftime(DF)
		return current_date

	date_begin = fields.Date('Begin date', default=_default_date, index=True)


class StandardRoutine(models.Model):
	"""docstring for StandardRoutine"""
	
	_name = 'standard.routine'
	_inherit = 'project.project'

