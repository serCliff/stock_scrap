# -*- coding: utf-8 -*-

from odoo import models, fields, api

import pdb


class Purchase(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_confirm(self):
        """Add the cost of product based on the last purchase cost"""
        for line in self.order_line:
            line.product_id.standard_price = line.price_unit
        return super(Purchase, self).button_confirm()


class Product(models.Model):
    _inherit = "product.template"

    @api.model
    def action_set_costs(self):
        for product_id in self.env['product.template'].search([]):
            have_purchases = self.env['purchase.order.line'].search([('product_id', '=', product_id.id)], order='id desc', limit=1)
            product_id.standard_price = have_purchases.price_unit

class StockScrap(models.Model):
    _inherit = "stock.scrap"

    cost = fields.Float(string="Precio de Coste", related="product_id.standard_price")