# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.model
    def create_copy_partner(self, number=100000):
        tmpl_partner = self.env.ref('pos_performance_test.res_partner_demo')
        for _i in range(number):
            tmpl_partner.copy()
            if _i % 10:
                print(">> finished: ", _i)
                self._cr.commit()

