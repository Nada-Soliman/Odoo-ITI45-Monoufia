from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    barcode2 = fields.Char("")



