# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ProductSyncHistory(models.Model):
    _name = 'product.sync.history'

    field_name = fields.Char(
        string="Field",
        required=True,
    )
    field_value = fields.Char(
        string="Field Value",
        required=True,
    )
    is_sync = fields.Boolean(
        string="Is Sync",
    )
    sync_date = fields.Datetime(
        string="Sync Date",
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
