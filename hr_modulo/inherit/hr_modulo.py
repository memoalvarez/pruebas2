# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class Hrmodulo(models.Model):
	_inherit = 'hr.employee'

	id_card_copy= fields.Many2many('ir.attachment', string="Identificación oficial")
	driving_license=fields.Many2many('ir.attachment', string="Licencia de conducir")
	curp=fields.Many2many('ir.attachment', string="CURP")
	rfc=fields.Many2many('ir.attachment', string="RFC")
	comprobante_de_domicilio=fields.Many2many('ir.attachment', string="Comprobante de domicilio")
	acta_de_nacimiento=fields.Many2many('ir.attachment', string="Acta de nacimiento")
	numero_de_seguro_social=fields.Many2many('ir.attachment', string="Numero de seguro social")
	comprobante_de_estudios=fields.Many2many('ir.attachment', string="Comprbante de estudios")
	certificaciones=fields.Many2many('ir.attachment', string="Certificaciones")
	carta_de_recomendacion=fields.Many2many('ir.attachment', string="Carta de recomendación")
	hoja_de_retencion_para_credito_infonavit=fields.Many2many('ir.attachment', string="Hoja de retención para credito infonavit")
	hoja_de_retencion_para_credito_fonacot=fields.Many2many('ir.attachment', string="Hoja de retención para credito fonacot")
	carta_de_no_antecedentes_penales=fields.Many2many('ir.attachment', string="Carta de no antecedentes penales")

	
