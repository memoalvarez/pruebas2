# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'crm.lead'

	agente_de_compra=fields.Char(string="Agente de compra")



	