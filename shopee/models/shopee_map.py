from odoo import models, fields, api
from ....addons import product
from ....addons import stock

class ShopeeMap(models.Model):
    _name = "shopee.map"
    _description = "A relation where each entry maps a product on Shopee to a product on Odoo."

    name = fields.Char("Shopee SKU", required=True)
    product_id = fields.Many2one("product.product", string="Odoo SKU", ondelete="set null")
    shopee_price = fields.Integer("Shopee Price", required=True)