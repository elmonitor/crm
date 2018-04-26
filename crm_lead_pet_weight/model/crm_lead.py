# -*- coding: utf-8 -*-
# Copyright 2017 David Vidal - Tecnativa S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    pet_weight = fields.Float("Peso de la mascota")

    @api.model
    def _lead_create_contact(self, name, is_company, parent_id=False):
        """Add trade name to partner."""
        return (super(CrmLead,
                      self.with_context(default_pet_weight=self.pet_weight)
                      )._lead_create_contact(name, is_company, parent_id))

    @api.multi
    def _onchange_partner_id_values(self, partner_id):
        """Recover pet_weight from partner if available."""
        result = super(CrmLead, self)._onchange_partner_id_values(partner_id)
        if partner_id:
            partner = self.env["res.partner"].browse(partner_id)
            if partner.pet_weight:
                result.update({"pet_weight": partner.pet_weight})
        return result
