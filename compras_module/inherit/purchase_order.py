# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	ficha_tecnica=fields.Many2many("ir.attachment", string="Ficha técnica")

	usuario_requisicion = fields.Many2one("res.partner", string="Usuario requisicion")