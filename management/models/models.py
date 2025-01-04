from odoo import models, fields

class Material(models.Model):
    _name = 'material.management' 
    _description = 'Material Management'  
    
    kode = fields.Char(string='Nama', required=True)  
    nama = fields.Char(string='Alamat')  
    tipe_material = fields.Selection(
        [('consumable', 'Consumable'), 
         ('stockable', 'Stockable'), 
         ('service', 'Service')],
        string='Tipe Material', 
        required=True
    )  
