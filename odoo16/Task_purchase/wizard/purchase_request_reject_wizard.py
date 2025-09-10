from odoo import models, fields,api

class PurchaseRequestRejectWizard(models.TransientModel):
    _name = 'purchase.request.reject.wizard'
    _description = 'Purchase Request Reject Wizard'

    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Request', required=True)
    rejection_reason = fields.Text(string='Rejection Reason', required=True)

    def action_confirm(self):
        self.purchase_request_id.write({
            'state': 'rejected',
            'rejection_reason': self.rejection_reason,
        })