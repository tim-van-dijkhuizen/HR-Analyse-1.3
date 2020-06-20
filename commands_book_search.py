from base_app import App
from base_command import Command

class CommandBookSearch(Command):

    def getUsage(self):
        return 'book/search'

    def execute(self, args):
        bookService = App.instance.getService('books')
        bookItemsService = App.instance.getService('bookItems')

        # Find book
        query = self.askQuestion("What book are you looking for?")
        books = bookService.searchBooks(query)

        self.showEmpty()
        self.showInfo('id - title - authorId - year - country - language - pages')

        # Show message when there are no results
        if not books:
            self.showError('No books match the given criteria')

        # Print books
        for book in books:
            self.showLine()
            self.showInfo(book)

            # Print book items
            bookItems = bookItemsService.getBookItemsByBook(book.id)
            
            self.showEmpty()
            self.showInfo('Available book item ID\'s:')

            for bookItem in bookItems:
                self.showInfo(' - ' + str(bookItem.id))

        self.showEmpty()