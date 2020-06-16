from base_command import Command

class CommandBookItemList(Command):

    def getUsage(self):
        return 'book-item/list'

    def execute(self, app, args):
        bookItemsService = app.getService('bookItems')

        self.showEmpty()
        self.showInfo('id - bookId')
        self.showLine()

        for bookItem in bookItemsService.getBookItems():
            self.showInfo(bookItem)

        self.showEmpty()