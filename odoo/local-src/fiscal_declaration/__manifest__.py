# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Fiscal Declaration",
    "description": """
        Track client invoices declared at Fiscal authority like Urssaf""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["account"],
    "data": [
        "views/account_move.xml",
        "security/ir.model.access.csv",
        "views/fiscal_declaration.xml",
    ],
    "demo": [],
}
