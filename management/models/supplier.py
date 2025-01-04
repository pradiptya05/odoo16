from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Supplier(models.Model):
    _name = 'supplier.management'  
    _description = 'Supplier Management'  
    
    name = fields.Char(string='Nama', required=True)  
    alamat = fields.Text(string='Alamat')  
    phone = fields.Char(string='Phone', required=True)  
    
    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if not re.match(r'^\d{10,15}$', record.phone):
                raise ValidationError("Nomor telepon harus terdiri dari 10 hingga 15 digit angka.")
