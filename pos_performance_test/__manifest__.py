# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Performance Test',
    'version': '1.1',
    'summary': 'POS Performance Test',
    'sequence': 30,
    'description': """
    POS Performance - POS Loading Fast - POS Speed Up
    """,
    'category': 'Point of Sale',
    'depends': [
        'point_of_sale'
    ],
    'data': [
        # data
        'data/product_data.xml',
        'data/partner_data.xml',
        'data/product_image_data.xml',
        'data/ir_cron_data.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'price': 150,
    'currency': 'EUR',
    'license': 'OPL-1',
    'support': 'fauniq.erp@gmail.com',
    'author': "Fauniq",
    'website': 'www.fauniq.com',
    'images': ['images/main_image.png'],
    'installable': True,
    'application': False,
    'auto_install': False
}