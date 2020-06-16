from base_command import Command
from helpers_validation_helper import ValidationHelper

class CommandBookEdit(Command):

    def getUsage(self):
        return 'book/edit <bookId>'

    def execute(self, app, args):
        bookService = app.getService('books')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Get book by id
        book = bookService.getBookById(args[0])

        if book == None:
            self.showError('Invalid book')

        # Update book
        book.title = self.askQuestion('Enter the title:', book.title)
        book.authorId = self.askQuestion('Enter the authorId:', book.authorId)
        book.year = self.askQuestion('Enter the year:', book.year)
        book.country = self.askQuestion('Enter the country:', book.country)
        book.languages = self.askQuestion('Enter the languages:', book.languages)
        book.pages = self.askQuestion('Enter the number of pages:', book.pages)

    	# Try to save
        if bookService.saveBook(book):
            self.showInfo('Successfully saved book')
        else:
            ValidationHelper.printErrorList(book)