# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class ProductProduct(models.Model):

    _inherit = 'product.product'

    @api.model
    def create_copy_product(self, number=100000):
        template_product = self.env.ref('pos_performance_test.product_product_tshirt')
        for _i in range(number):
            new_product = template_product.copy()
            new_product.image = template_product.image
            if _i % 10:
                print(">> finished: ", _i)
                self._cr.commit()

    @api.model
    def update_product_image(self):
        template_product = self.env.ref('pos_performance_test.product_product_tshirt')
        for product in self.search([], order='id'):
            if not product.image:
                product.image = template_product.image
                self._cr.commit()

