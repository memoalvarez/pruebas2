# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'sales_module'

	agente_de_venta = fields.Chair(string="Agente de venta")
    importe_de_venta = fields.Float(string="Importe de venta")
	

	