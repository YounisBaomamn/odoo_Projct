
# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materials(models.Model):
    _name = 'material.materials'
    
    sound_equipment = fields.Char(string="Name" )
    
    # audio_device = fields.Boolean( string='Audio Device',)
    # cameras = fields.Boolean( string='Cameras',)
    # lamps = fields.Boolean(string='Lamps',)
    
    projection_equipment_ids = fields.Many2many( string='Projection Equipment', comodel_name='material.equipment',)
    
    


