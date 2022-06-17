from odoo import _, api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    
    item_id = fields.Many2one('item.item')    