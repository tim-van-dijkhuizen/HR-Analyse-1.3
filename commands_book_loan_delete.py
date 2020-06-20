from base_app import App
from base_command import Command

class CommandBookLoanDelete(Command):

    def getUsage(self):
        return 'book-loan/delete <bookLoanId>'

    def execute(self, args):
        bookLoanService = App.instance.getService('bookLoans')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Find book loan
        bookLoan = bookLoanService.getBookLoanById(args[0])

        if bookLoan == None:
            self.showError('Invalid book loan')

        # Try to delete
        if bookLoanService.deleteBookLoan(bookLoan):
            self.showInfo('Successfully deleted book loan')
        else:
            self.showError('Failed to delete book loan')