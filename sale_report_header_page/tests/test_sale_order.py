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

    def test_on_change_term_template(self):
        self.sale_order.header_page_id = self.header_page
        self.sale_order._onchange_header_page_id()
        self.assertEqual(
            self.sale_order.header_page, "<p>Terms template, customer: Ready Mat</p>"
        )
