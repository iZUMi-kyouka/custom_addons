from .... import models, fields, api
from ....addons import product
from ....addons import stock
from datetime import datetime

class TokopediaOrder(models.Model):
    _name = "tokopedia.order"
    _description = "An instance of a unique order made on Tokopedia."

    invoice_no = fields.Char("Invoice No.", required=True)
    write_date = fields.Datetime("Date Added", default=datetime.now(), readonly=True)
    tokopedia_id = fields.Many2one("tokopedia.map", string="Tokopedia SKU", required=True)
    quantity = fields.Integer("Quantity", required=True, default=1)
    total_amount = fields.Integer("Total Amount", required=True)
    payment_date = fields.Date("Payment Date", required=True)
    delivery_date = fields.Date("Delivery Date")
    last_status = fields.Selection(
        string="Order Status",
        selection=[("done", "Done"), ("delivering", "Delivering")]
    )
    tracking_id = fields.Char("Tracking ID")

    @api.model
    def create(self, vals):
        order = super(TokopediaOrder, self).create(vals)
        map_entry = self.env['tokopedia.map'].search([('name', '=', order.tokopedia_id.name)], limit=1)
        if map_entry:
            product = map_entry.product_id
            stock_quant = self.env['stock.quant'].search([('product_id', '=', product.id)], limit=1)
            if stock_quant:
                stock_quant.ensure_one()
                stock_quant.quantity -= order.quantity

                stock_quant.sudo().write({'quantity': stock_quant.quantity})
        return order