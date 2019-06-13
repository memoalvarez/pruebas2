# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class ContactModule(models.Model):
	_inherit = 'res.partner'

	canal_de_distribucion=fields.Many2one("canal.de.distribucion", string="Canal de distribución")
	
	

	