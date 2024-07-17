from .... import models, fields, api

class TokopediaOrder(models.Model):
    _name = "tokopedia.order"
    _description = "An instance of a unique order made on Tokopedia."

    invoice_no = fields.Char("Invoice No.", required=True)
    sku_id = fields.Many2one("tokopedia.product", string="SKU")
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
        product = order.sku_id
        if product:
            product.stock -= order.quantity
            product.sudo().write({'stock': product.stock})
        return order

        