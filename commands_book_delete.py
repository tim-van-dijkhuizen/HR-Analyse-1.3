from base_app import App
from base_command import Command

class CommandBookDelete(Command):

    def getUsage(self):
        return 'book/delete <bookId>'

    def execute(self, args):
        bookService = App.instance.getService('books')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Find book
        book = bookService.getBookById(args[0])

        if book == None:
            self.showError('Invalid book')

        # Try to delete
        if bookService.deleteBook(book):
            self.showInfo('Successfully deleted book')
        else:
            self.showError('Failed to delete book')