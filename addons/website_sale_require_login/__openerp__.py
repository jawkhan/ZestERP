# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería, S.L. - Jairo Llopis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Require login to checkout",
    "summary": "Force users to login for buying",
    "version": "9.0.1.0.0",
    "category": "Website",
    "website": "http://www.antiun.com",
    "author": "Tecnativa, "
              "LasLabs, "
              "Zest ERP Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "website_sale_suggest_create_account",
    ],
    "data": [
        "views/assets.xml",
        "views/website_sale.xml",
    ],
}
