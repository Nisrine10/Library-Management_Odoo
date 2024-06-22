from odoo import models, fields, api, exceptions
from datetime import date, timedelta

class Loan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    borrower_id = fields.Many2one('library.borrower', string='Borrower', required=True)
    book_id = fields.Many2one('library.book', string='Book', required=True, domain="[('available_copies','>',0)]")
    loan_date = fields.Date(string='Loan Date', required=True, default=fields.Date.today)
    return_date = fields.Date(string='Return Date', required=True)
    state = fields.Selection([
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned')
    ], string='Status', default='borrowed', required=True)

    @api.model
    def create(self, vals): # Méthode surchargée pour la création d'un prêt
        borrower_id = vals.get('borrower_id')
        if borrower_id:
            existing_loans = self.search([('borrower_id', '=', borrower_id), ('state', '=', 'borrowed')])
            if existing_loans:
                # Lève une erreur si l'emprunteur a des livres non retournés
                raise exceptions.ValidationError("The borrower has unreturned books and cannot borrow another one.")
        loan = super(Loan, self).create(vals)
        if loan.book_id:
            loan.book_id._compute_available_copies() # Met à jour le nombre de copies disponibles
        return loan

    def write(self, vals):  # Méthode surchargée pour la modification d'un prêt apres le return
        res = super(Loan, self).write(vals)
        for loan in self:
            if 'state' in vals and vals['state'] == 'returned':
                loan.book_id._compute_available_copies()
        return res

    """
   
    @api.constrains('loan_date', 'return_date')
    def _check_loan_dates(self):
        for loan in self:
            if loan.return_date < loan.loan_date:
                raise exceptions.ValidationError("Return date must be after loan date.")

    
    @api.model
    def send_loan_due_reminders(self):
        today = date.today()
        due_reminders = self.search([('state', '=', 'borrowed'), ('return_date', '=', today + timedelta(days=1))])
        template_id = self.env.ref('your_module.email_template_loan_due_reminder').id
        for loan in due_reminders:
            self.env['mail.template'].browse(template_id).send_mail(loan.id, force_send=True)

"""