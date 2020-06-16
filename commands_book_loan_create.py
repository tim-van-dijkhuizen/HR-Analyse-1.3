from base_command import Command
from helpers_validation_helper import ValidationHelper
from models_book_loan import BookLoan

class CommandBookLoanCreate(Command):

    def getUsage(self):
        return 'book-loan/create'

    def execute(self, app, args):
        bookLoanService = app.getService('bookLoans')

        # Get arguments
        bookItemId = self.askQuestion('Enter the book item ID:')
        customerId = self.askQuestion('Enter the customer ID:')

        # Create book loan
        bookLoan = BookLoan({
            'bookItemId': bookItemId,
            'customerId': customerId
        })

    	# Try to save
        if bookLoanService.saveBookLoan(bookLoan):
            self.showInfo('Successfully created book loan')
        else:
            ValidationHelper.printErrorList(bookLoan)