# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'crm.lead'

	ingreso_conectividad=fields.float(string="Ingreso conectividad") 
	ingreso_de_ingenieria=fields.float(string="Ingreso de ingenieria")


