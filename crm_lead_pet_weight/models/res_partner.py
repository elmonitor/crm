# -*- coding: utf-8 -*-
# Copyright 2017 David Vidal - Tecnativa S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "res.partner"

    pet_weight = fields.Float("Peso de la mascota")
