from odoo import models, fields, api

class Category(models.Model):
    _name = 'library.category'
    _description = 'Library Category'

    name = fields.Char(string='Name', required=True)
    book_ids = fields.One2many('library.book', 'category_id', string='Books')
    book_count = fields.Integer(string='Number of Books', compute='_compute_book_count')
    book_count_str = fields.Char(string='Book Count String', compute='_compute_book_count_str', store=True)

    @api.depends('book_ids')
    def _compute_book_count(self):
        for category in self:
            category.book_count = len(category.book_ids) # Compte le nombre de livres dans la catégorie

    @api.depends('book_count')
    def _compute_book_count_str(self):
        for category in self:
            category.book_count_str = str(category.book_count) + ' book(s)' # Convertit le nombre de livres en chaîne de caractères
