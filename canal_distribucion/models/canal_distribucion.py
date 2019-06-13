# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class Canaldedistribucion(models.Model):

	_name = "canal.de.distribucion"
	_description = 'Modulo para saber el canal de distribucion'


	name=fields.Char(string="Canal de distribución")
	descripcion=fields.Many2one("canal.de.distribucion", string="Categoria padre")