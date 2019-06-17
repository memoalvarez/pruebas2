# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class MontoMaximo(models.Model):

	_name = "monto.maximo"
	_description = 'Monto maximo para compras'


	currency_id = fields.Many2one('res.currency', 'Moneda')
	monto_maximo = fields.Float(string="Monto máximo")
	user_id = fields.Many2one('res.users', 'Usuario')