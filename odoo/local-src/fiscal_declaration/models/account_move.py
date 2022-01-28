# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    declaration_id = fields.Many2one(
        string="Fiscal Declaration", comodel_name="fiscal.declaration"
    )
    declaration_date = fields.Date(
        string="Declaration Date", related="declaration_id.declaration_date"
    )
