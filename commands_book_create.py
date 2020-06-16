from base_command import Command
from helpers_validation_helper import ValidationHelper
from models_book import Book

class CommandBookCreate(Command):

    def getUsage(self):
        return 'book/create'

    def execute(self, app, args):
        bookService = app.getService('books')

        # Get arguments
        title = self.askQuestion('Enter the title:')
        authorId = self.askQuestion('Enter the author ID:')
        year = self.askQuestion('Enter the year:')
        country = self.askQuestion('Enter the country:')
        language = self.askQuestion('Enter the language:')
        pages = self.askQuestion('Enter the number of pages:')

        # Create book
        book = Book({
            'title': title,
            'authorId': authorId,
            'year': year,
            'country': country,
            'language': language,
            'pages': pages
        })

    	# Try to save
        if bookService.saveBook(book):
            self.showInfo('Successfully created book')
        else:
            ValidationHelper.printErrorList(book)