# # -*- coding: utf-8 -*-

from odoo import models, fields, api

class Organizer(models.Model):
    _name='organizer.organizers'

    

    last_name = fields.Char(string="Last Name", )
    first_name = fields.Char(string="First Name", )
    phone = fields.Char(string="Phone")
    mail = fields.Char(string="Mail", )
    aselection = fields.Selection([('master', 'Mr'),('mistress', 'Msr')], string='Aselection ', default='master',)
    event_id = fields.Many2one("event.event" , ondelete='cascade' ,string="Event",required=True)
    companys_types = fields.Selection([('individual', 'Individual'),('company', 'Company')],  default='company',)
    companys =fields.Boolean(string='field_name',default=False)
    
    field_name_ids = fields.Many2one('res.partner',ondelete='cascade', )
    

    
    
    






    