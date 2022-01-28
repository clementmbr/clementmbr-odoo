# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class FiscalDeclaration(models.Model):
    _name = "fiscal.declaration"
    _description = "Fiscal Declaration"  # TODO

    name = fields.Char(readonly=True)
    declaration_date = fields.Date(
        string="Date", help="Date of the declaration", required=True
    )
    move_ids = fields.One2many(
        string="Invoices declared",
        comodel_name="account.move",
        inverse_name="declaration_id",
    )


    @api.model
    def create(self, vals):
        date = vals.get("declaration_date")
        if date:
            vals["name"] = _("Declaration ") + date
        return super().create(vals)
