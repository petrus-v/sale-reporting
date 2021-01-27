# © 2020 Pierre Verkest <pierreverkest84@gmail.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale header page",
    "summary": "Add header page on sale order/quotation report",
    "category": "Sales/Sales",
    "version": "14.0.1.0.0",
    "author": "Pierre Verkest, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/sale-reporting",
    "license": "AGPL-3",
    "depends": [
        "base_comment_template",
        "sale_management",
    ],
    "data": [
        "views/sale_views.xml",
        "report/sale_report_templates.xml",
    ],
    "installable": True,
}
