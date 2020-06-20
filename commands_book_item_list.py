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

        for bookItem in bookItemsService.getBookItems():
            self.showInfo(bookItem)

        self.showEmpty()