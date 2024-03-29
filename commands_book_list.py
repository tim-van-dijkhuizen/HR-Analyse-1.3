from base_app import App
from base_command import Command

class CommandBookList(Command):

    def getUsage(self):
        return 'book/list'

    def execute(self, args):
        bookService = App.instance.getService('books')

        self.showEmpty()
        self.showInfo('id - title - authorId - year - country - language - pages')
        self.showLine()

        # Get books
        books = bookService.getBooks()

        # Show message when there are no results
        if not books:
            self.showError('No books found')

        for book in books:
            self.showInfo(book)

        self.showEmpty()