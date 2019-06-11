# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'crm.lead'

	ingreso_conectividad=fields.Float(string="Ingreso conectividad") 
	ingreso_de_ingenieria=fields.Float(string="Ingreso de ingenieria")


