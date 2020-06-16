from base_command import Command

class CommandBookLoanList(Command):

    def getUsage(self):
        return 'book-loan/list'

    def execute(self, app, args):
        bookLoansService = app.getService('bookLoans')

        self.showEmpty()
        self.showInfo('id - bookItemId - customerId')
        self.showLine()

        for bookLoan in bookLoansService.getBookLoans():
            self.showInfo(bookLoan)

        self.showEmpty()