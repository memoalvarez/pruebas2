# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class ContactModule(models.Model):
	_inherit = 'res.partner'

	#importancia_del_cliente=fields.Many2one("importancia.cliente", string="Importancia del cliente")
	
	

	