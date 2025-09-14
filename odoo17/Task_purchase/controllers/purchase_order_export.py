from odoo import http
from odoo.http import request
import io
import xlsxwriter

class PurchaseOrderExport(http.Controller):

    @http.route('/purchase_order/export_excel', type='http', auth='user', csrf=False)
    def export_purchase_orders_to_excel(self, **kwargs):
        # Retrieve selected order IDs from request parameters
        selected_order_ids = kwargs.get('order_ids')
        if selected_order_ids:
            # Convert comma-separated string of IDs to a list of integers
            selected_order_ids = [int(order_id) for order_id in selected_order_ids.split(',')]
        else:
            return request.not_found()  # Return 404 if no order IDs provided

        # Create an in-memory Excel file
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Purchase Orders')

        # Define headers and formats
        headers = ['Order Reference', 'Order ID', 'Description Note', 'Vendor', 'Date Order', 'Total Amount']
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3', 'border': 1})
        cell_format = workbook.add_format({'border': 1})

        # Write headers
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, header_format)

        # Fetch only the selected purchase orders and write data rows
        purchase_orders = request.env['purchase.order'].sudo().browse(selected_order_ids)
        row = 1
        for order in purchase_orders:
            worksheet.write(row, 0, order.name, cell_format)
            worksheet.write(row, 1, order.order_id, cell_format)
            worksheet.write(row, 2, order.note_des, cell_format)
            worksheet.write(row, 3, order.partner_id.name, cell_format)
            worksheet.write(row, 4, order.date_order.strftime('%Y-%m-%d') if order.date_order else '', cell_format)
            worksheet.write(row, 5, order.amount_total, cell_format)
            row += 1

        workbook.close()
        output.seek(0)

        # Set up the HTTP response headers for the file download
        response = request.make_response(
            output.getvalue(),
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', 'attachment; filename=Purchase_Orders.xlsx;')
            ]
        )
        output.close()

        return response