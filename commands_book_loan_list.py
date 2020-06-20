from base_app import App
from base_command import Command

class CommandBookLoanList(Command):

    def getUsage(self):
        return 'book-loan/list'

    def execute(self, args):
        bookLoansService = App.instance.getService('bookLoans')

        self.showEmpty()
        self.showInfo('id - bookItemId - customerId')
        self.showLine()

        # Get book loans
        bookLoans = bookLoansService.getBookLoans()

        # Show message when there are no results
        if not bookLoans:
            self.showError('No book loans found')

        for bookLoan in bookLoans:
            self.showInfo(bookLoan)

        self.showEmpty()