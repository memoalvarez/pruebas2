# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class MontoMaximo(models.Model):

	_name = "contabilidad.modulo"
	_description = 'Captura tus facturas a clientes extrangeros'


	name=fields.Char(string="Facturas USD")