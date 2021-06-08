# # -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomPartner(models.Model):
    _inherit = 'res.partner'
    
    partner = fields.Boolean(string='Partner')
    
   