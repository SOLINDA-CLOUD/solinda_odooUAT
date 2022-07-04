from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.constrains('ref')
    def _check_mobile_unique(self):
        if self.ref:
            ref_counts = self.search_count(
                [('ref', '=', self.ref), ('id', '!=', self.id)])
            print(self.ref)
            if ref_counts > 0:
                raise ValidationError("Reference number already exists!")
        else:
            return

    @api.depends('invoice_line_ids.qty_received_account')
    def _compute_total_qty_received(self):
        for this in self:
            this.total_qty_received = sum(
                this.invoice_line_ids.mapped('qty_received_account'))

    total_qty_received = fields.Integer(
        compute='_compute_total_qty_received', string='Qty Received', store=True)
    invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice lines',
                                       copy=False, readonly=True,
                                       domain=[
                                           ('exclude_from_invoice_tab', '=', False)],
                                       states={'draft': [('readonly', False)]})


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    purchase_line_id = fields.Many2one(
        'purchase.order.line', 'Purchase Order Line', ondelete='set null', index=True)
    qty_received_account = fields.Float(related='purchase_line_id.qty_received', store=True, string="Qty Received")
