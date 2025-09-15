from symtable import Class

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    note_des = fields.Char("Description Note")



class StockMove(models.Model):
    _inherit = 'stock.move'

    note_desc = fields.Char(string="Description Notes")

    @api.model
    def create(self, vals):
        # Create the stock move first
        move = super(StockMove, self).create(vals)

        # Check if the move is linked to a sale.order.line through the sale_line_id field
        if move.sale_line_id:
            move.note_desc = move.sale_line_id.note_desc  # Copy custom_note from sale.order.line
        return move


