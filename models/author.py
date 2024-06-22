from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image')
    book_ids = fields.One2many('library.book', 'author_id', string='Books')
