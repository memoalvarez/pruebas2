# -*- coding: utf-8 -*-

from odoo import models, api, fields, exceptions


class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	data_sheet = fields.Many2many('ir.attachment', string="Ficha técnica")


	@api.multi
	def button_confirm(self):

		objeto = self.env['monto.maximo'].search([['currency_id.id', '=', self.currency_id.id]], limit=1)

		monto_maximo = objeto.monto_maximo
		usuario = objeto.user_id
		usuario_actual = self.env.uid

		if self.amount_total > monto_maximo:

			if usuario_actual != usuario.id:
				raise exceptions.ValidationError('Monto no permitido, pide ayuda a ' + usuario.name)
			else:
				pass	


		for order in self:
			if not order.partner_id.quality_certificate:
				raise exceptions.ValidationError('El proveedor no cuenta con certificado de calidad vigente')
				

		res = super(PurchaseOrder, self).button_confirm()

		return res