from .... import fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A property's type"

    name = fields.Char("Name", required=True)