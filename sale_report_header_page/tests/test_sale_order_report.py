# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestSaleOrder(TransactionCase):
    def setUp(self):
        super().setUp()
        self.header_page = self.env["base.comment.template"].create(
            {
                "name": "My sale report header page",
                "text": "<p>Terms template, customer: ${object.partner_id.name}</p>",
            }
        )
        self.sale_order = self.env.ref("sale.sale_order_2")
        self.sale_order.header_page_id = self.header_page
        self.sale_order._onchange_header_page_id()

    def test_report(self):
        report = self.env["ir.actions.report"].search(
            [("report_name", "=", "sale.report_saleorder")]
        )
        report.ensure_one()
        generated_content, _ = report._render_qweb_html([self.sale_order.id])
        self.assertRegex(
            generated_content.decode(), ".*Terms template, customer: Ready Mat.*"
        )
