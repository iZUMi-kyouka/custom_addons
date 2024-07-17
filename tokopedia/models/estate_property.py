from .... import fields, models
import datetime as dt

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    active = fields.Boolean(default=True, readonly=True)
    name = fields.Char('Title', required=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer = fields.Many2one('res.partner', string="Buyer", copy=False)
    salesperson = fields.Many2one('res.users', string="Salesperson", default=lambda self: self.env.user)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', copy=False, default=fields.Date.today() + dt.timedelta(days=90))
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly="true", copy=False)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )