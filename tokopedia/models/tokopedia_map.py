from .... import models, fields, api
from ....addons import product
from ....addons import stock

class TokopediaMap(models.Model):
    _name = "tokopedia.map"
    _description = "A relation where each entry maps a product on Tokopedia to a product on Odoo."

    name = fields.Char("Tokopedia SKU", required=True, unique=True)
    product_id = fields.Many2one("product.product", string="Odoo SKU", required=True)
    tokopedia_price = fields.Integer("Tokopedia Price", required=True)