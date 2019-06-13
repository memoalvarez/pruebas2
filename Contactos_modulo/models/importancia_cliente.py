# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class ImportanciaCliente(models.Model):

	_name = "importancia.cliente"
	_description = 'modelo para identificar la importancia del cliente'


	name=fields.Char(string="Nivel de importancia")
	descripcion=fields.Char(string="Descripción")


	