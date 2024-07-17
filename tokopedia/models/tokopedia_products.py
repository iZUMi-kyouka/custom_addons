from .... import fields, models

class TokopediaProduct(models.Model):
    _name = "tokopedia.product"
    _description = "An instance of a unique product sold on Tokopedia."

    name = fields.Char("SKU", required=True)
    product_name = fields.Text("Name", required=True)
    stock = fields.Integer("Stock", required=True)