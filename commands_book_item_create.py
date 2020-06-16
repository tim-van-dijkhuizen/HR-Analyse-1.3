from base_command import Command
from helpers_validation_helper import ValidationHelper
from models_book_item import BookItem

class CommandBookItemCreate(Command):

    def getUsage(self):
        return 'book-item/create'

    def execute(self, app, args):
        bookItemService = app.getService('bookItems')

        # Get arguments
        bookId = self.askQuestion('Enter the book ID:')

        # Create book item
        bookItem = BookItem({
            'bookId': bookId
        })

    	# Try to save
        if bookItemService.saveBookItem(bookItem):
            self.showInfo('Successfully created book item')
        else:
            ValidationHelper.printErrorList(bookItem)