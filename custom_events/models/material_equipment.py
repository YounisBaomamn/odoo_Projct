# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material_equipment(models.Model):
    _name = 'material.equipment'
    
    name_equipment= fields.Char(string='Name Equipment', )
    