from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author', required=True)
    category_id = fields.Many2one('library.category', string='Category', required=True)
    image = fields.Binary(string='Image')
    total_copies = fields.Integer(string='Total Copies', required=True, default=1)
    available_copies = fields.Integer(string='Available Copies', compute='_compute_available_copies', store=True)
    loan_ids = fields.One2many('library.loan', 'book_id', string='Loans')

    @api.depends('loan_ids', 'total_copies')
    def _compute_available_copies(self):
        for book in self:
            loaned_count = self.env['library.loan'].search_count([('book_id', '=', book.id), ('state', '=', 'borrowed')])
            book.available_copies = book.total_copies - loaned_count

    def name_get(self):
        result = []
        for book in self:
            name = book.title
            result.append((book.id, name))
        return result
