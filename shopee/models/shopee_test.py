from .... import models, fields, api
from ....addons import product
from ....addons import stock

class ShopeeTest(models.Model):
    _name = "shopee.test"
    _description = "Test model."

    name = fields.Char("Test Name", required=True)
    test_class = fields.Char("Test Class", required=True)