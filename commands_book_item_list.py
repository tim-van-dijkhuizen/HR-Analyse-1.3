from base_app import App
from base_command import Command

class CommandBookItemList(Command):

    def getUsage(self):
        return 'book-item/list'

    def execute(self, args):
        bookItemsService = App.instance.getService('bookItems')

        self.showEmpty()
        self.showInfo('id - bookId')
        self.showLine()

        # Get book items
        bookItems = bookItemsService.getBookItems()

        # Show message when there are no results
        if not bookItems:
            self.showError('No book items found')

        for bookItem in bookItems:
            self.showInfo(bookItem)

        self.showEmpty()