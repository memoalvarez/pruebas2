# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class MontoMaximo(models.Model):

	_name = "importancia.cliente"
	_description = 'modelo para identificar la importancia del cliente'


	nivel_de_importancia=fields.Char(string="Nivel de importancia")
	descripcion=fields.Char(string="Descripción")


	