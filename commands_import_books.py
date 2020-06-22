import json
from base_app import App
from base_command import Command
from helpers_file_helper import FileHelper
from helpers_validation_helper import ValidationHelper
from models_author import Author
from models_book import Book

class CommandImportBooks(Command):

    requiredKeys = { 'author', 'title', 'year', 'country', 'language', 'pages' }

    def getUsage(self):
        return 'import/books'

    def execute(self, args):
        authorService = App.instance.getService('authors')
        bookService = App.instance.getService('books')

        # Get json from file
        rawPath = self.askQuestion('Which file would you like to import?')
        filePath = FileHelper.createFilePath(rawPath, True)

        if not filePath.exists():
            self.showError('Json file doesn\'t exist')

        try:
            with open(filePath, 'r', encoding = 'utf8') as fileContent:
                data = json.load(fileContent)
        except json.JSONDecodeError:
            self.showError('Failed to load json. The file contains invalid json.')
        except Exception:
            self.showError('Failed to load json. Unable to read file contents.')

        # Validate the json structure
        self._validateJson(data)

        # Create authors
        authorNames = set(map(lambda a: a['author'], data))
        authors = {}

        for authorName in authorNames:
            parts = authorName.split(' ')
            firstName = parts.pop(0)
            lastName = ' '.join(parts)

            # Create author
            author = Author({
                'firstName': firstName,
                'lastName': lastName
            })

            # Save and map it
            if not authorService.saveAuthor(author):
                ValidationHelper.printErrorList(author)
                raise Exception('Unable to save author: ' + authorName)

            authors[authorName] = author

        # Create books
        for bookRow in data:
            author = authors[bookRow['author']]

            book = Book({
                'title': bookRow['title'],
                'authorId': author.id,
                'year': bookRow['year'],
                'country': bookRow['country'],
                'language': bookRow['language'],
                'pages': bookRow['pages']
            })

            # Try to save
            if not bookService.saveBook(book):
                ValidationHelper.printErrorList(book)
                raise Exception('Unable to save book: ' + bookRow['title'])

        self.showInfo('Successfully imported books')

    def _validateJson(self, json):
        if not isinstance(json, list):
            self.showError('Json root element must be a list')

        # Make sure all objects contain at least the required keys
        for item in json:
            keys = set(item.keys())

            if not self.requiredKeys.issubset(keys):
                self.showError('Missing one or more required object keys')
