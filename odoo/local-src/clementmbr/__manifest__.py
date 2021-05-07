# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Clement Auto-entrepreneur",
    "description": """ yo """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": [
        # Odoo CE official modules
        "calendar",
        "contacts",
        "project",
        "account",
        "sale_management",
        "l10n_fr_fec",
        "fetchmail",
        # "hr_timesheet",
        # OCA https://github.com/OCA/web
        "web_responsive",
        "web_notify",
        "web_dialog_size",
        # "web_listview_range_select",
        # # OCA https://github.com/OCA/social
        "mail_debrand",
        # # OCA https://github.com/OCA/server-brand
        "disable_odoo_online",
        "remove_odoo_enterprise",
        # OCA https://github.com/oca/account-financial-tools
        "account_menu",
        # # OCA https://github.com/OCA/l10n-france
        "l10n_fr_siret",
        "l10n_fr_department",
        "l10n_fr_state",
        # https://github.com/Openworx/backend_theme
        "backend_theme_v14",
        # https://github.com/OCA/account-invoicing
        "sale_timesheet_invoice_description",
    ],
    "data": [
        "data/clementmbr_data.xml",
        "report/report_templates.xml",
        "report/sale_report_templates.xml",
        "report/invoice_report_templates.xml",
    ],
    "demo": [],
}
