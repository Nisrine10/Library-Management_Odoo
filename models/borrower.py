from odoo import models, fields, api, exceptions

class Borrower(models.Model):
    _name = 'library.borrower'
    _description = 'Library Borrower'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone', required=True)
    address = fields.Text(string='Address')
    loan_ids = fields.One2many('library.loan', 'borrower_id', string='Loans')

    @api.constrains('loan_ids')
    def _check_active_loan(self):
        for borrower in self:
            active_loans = borrower.loan_ids.filtered(lambda loan: loan.state == 'borrowed')
            if len(active_loans) > 0:
                raise exceptions.ValidationError("You cannot take another book until you return the borrowed one.")
