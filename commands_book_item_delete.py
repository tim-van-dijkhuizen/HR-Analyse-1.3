from base_app import App
from base_command import Command

class CommandBookItemDelete(Command):

    def getUsage(self):
        return 'book-item/delete <bookItemId>'

    def execute(self, args):
        bookItemService = App.instance.getService('bookItems')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Find book item
        bookItem = bookItemService.getBookItemById(args[0])

        if bookItem == None:
            self.showError('Invalid book item')

        # Try to delete
        if bookItemService.deleteBookItem(bookItem):
            self.showInfo('Successfully deleted book item')
        else:
            self.showError('Failed to delete book item')