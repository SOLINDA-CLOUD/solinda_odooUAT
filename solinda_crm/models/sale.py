from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Other Information
    subject = fields.Char(string="Subject")
    attn_id = fields.Many2one('res.partner', string='Attn')
    email = fields.Char(related='attn_id.email', store=True)