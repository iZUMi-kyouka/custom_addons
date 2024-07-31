from odoo import models, fields, api
from odoo.exceptions import UserError
import base64

class TokopediaImportWizard(models.TransientModel):
    _name = 'tokopedia.import.wizard'
    _description = 'Tokopedia Order Import Wizard'

    file_data = fields.Binary('XLSX File', required=True, filters='*.xlsx')
    file_name = fields.Char('File Name')

    def import_orders(self):
        if not self.file_data:
            raise UserError('Please upload a file to import.')

        file_content = base64.b64decode(self.file_data)
        file_path = '/tmp/tokopedia_import.xlsx'

        with open(file_path, 'wb') as file:
            file.write(file_content)

        # Call the import method from the ShopeeOrder model
        self.env['tokopedia.order'].import_tokopedia_orders(file_path)

        return {'type': 'ir.actions.act_window_close'}