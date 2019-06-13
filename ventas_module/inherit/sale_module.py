# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'sale.order'

	agente_de_venta=fields.Char(string="Agente de venta")
	importe_de_venta=fields.Float(string="Importe de venta")
	

	