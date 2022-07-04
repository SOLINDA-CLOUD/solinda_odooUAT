from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    # @api.constrains('ref')
    # def _check_mobile_unique(self):
    #     ref_counts = self.search_count(
    #         [('ref', '=', self.ref), ('id', '!=', self.id)])
    #     print(ref_counts)
    #     if ref_counts > 0:
    #         raise ValidationError("Reference number already exists!")
