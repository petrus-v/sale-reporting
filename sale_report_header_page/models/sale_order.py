# Copyright 2021 Pierre Verkest <pierreverkest84@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    header_page_id = fields.Many2one(
        "base.comment.template",
        string="Header page",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    header_page = fields.Html(readonly=True, states={"draft": [("readonly", False)]})

    @api.onchange("header_page_id")
    def _onchange_header_page_id(self):
        if self.header_page_id:
            self.header_page = self.header_page_id.get_value(
                partner_id=self.partner_id.id if self.partner_id else None,
                model="sale.order",
                res_id=self.id,
                post_process=True,
            )
