from base_app import App
from base_model import Model
from helpers_validation_helper import ValidationHelper

class BookItem(Model):

    bookId = None

    def validate(self):
        bookService = App.instance.getService('books')

        if self.bookId == None:
            self.addError('bookId', 'Book is required')
            return False

        if bookService.getBookById(self.bookId) == None:
            self.addError('bookId', 'Book does not exist')
            return False

        return True

    def getBook(self):
        bookService = App.instance.getService('books')

        # Get book from database
        book = bookService.getBookById(self.bookId)

        if book == None:
            raise Exception('Book with id ' + self.bookId + ' does not exist')

        return book

    def __str__(self):
        id = str(self.id)
        bookId = str(self.bookId)

        return id + ' - ' + bookId

    @staticmethod
    def fromDataRow(row):
        return BookItem({
            'id': row[0],
            'bookId': row[1],
        })