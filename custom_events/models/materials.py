
# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materials(models.Model):
    _name = 'material.materials'
    
    name = fields.Char(string="Name" )
    Kinds_materials = fields.Selection(
        string='Kinds of Materials',
        selection=[
                   ('sound_equipment', 'Sound Equipment'),
                   ('projection_equipment', 'Projection Equipment')])
   
 
    
    


