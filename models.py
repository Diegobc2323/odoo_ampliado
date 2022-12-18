import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import time
from datetime import datetime



class Persona(models.Model):
    _name = 'libreria.persona'
    _description = 'Modelo de persona'

    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    nacionalidad = fields.Char(string="Nacionalidad", required=True)


#create autor model
class Autor(models.Model):
    _name = 'libreria.autor'
    _description = 'Modelo de autor'
    _inherit = 'libreria.persona'

    
    fecha_fallecimiento = fields.Date(string="Fecha de fallecimiento")
    libros = fields.One2many('libreria.libro', 'autor', string="Libros")
    edad = fields.Integer(string="Edad")
 
    
    @api.onchange('fecha_nacimiento')
    def _onchange_fecha_nacimiento(self):
        if self.fecha_nacimiento:
            self.edad = datetime.now().year - self.fecha_nacimiento.year
    
    @api.onchange('fecha_fallecimiento')
    def _onchange_fecha_fallecimiento(self):
        if self.fecha_fallecimiento:
            self.edad = self.fecha_fallecimiento.year - self.fecha_nacimiento.year
    
#create libro model
class Libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Modelo de libro'

    titulo = fields.Char(string="Titulo", required=True)
    autor = fields.Many2one('libreria.autor', string="Autor")
    fecha_publicacion = fields.Date(string="Fecha de publicacion", required=True)
    editorial = fields.Char(string="Editorial", required=True)
    precio = fields.Float(string="Precio", required=True)

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 5:
                raise ValidationError("El precio tiene que ser mayor a 5 euros")
    


#create lector model
class Lector(models.Model):
    _name = 'libreria.lector'
    _description = 'Modelo de lector'
    _inherit = 'libreria.persona'

    libros = fields.Many2many('libreria.libro', string="Libros")
    entero_1 = fields.Integer(string="Entero 1")
    entero_2 = fields.Integer(string="Entero 2")
    entero_3 = fields.Integer(string="Entero 3")
    media = fields.Float(string="Media")

    @api.onchange('entero_1', 'entero_2', 'entero_3')
    def _onchange_enteros(self):
        # average of integers
        self.media = (self.entero_1 + self.entero_2 + self.entero_3) / 3


class Vendedor(models.Model):
    _name = 'libreria.vendedor'
    _description = 'Modelo de vendedor'
    _inherit = 'libreria.persona'
    
    libros = fields.Many2many('libreria.libro', string="Libros")