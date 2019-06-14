# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	data_sheet = fields.Many2many('ir.attachment', string="Ficha técnica")


	