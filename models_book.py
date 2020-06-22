from base_app import App
from base_model import Model
from helpers_validation_helper import ValidationHelper

class Book(Model):

    title = None
    authorId = None
    year = None
    country = None
    language = None
    pages = None

    def validate(self):
        authorService = App.instance.getService('authors')

        if self.title == None or len(self.title) == 0:
            self.addError('title', 'Title is required')
            return False

        if len(self.title) > 255:
            self.addError('title', 'Title cannot be longer than 255 characters')
            return False

        if self.authorId == None:
            self.addError('authorId', 'Author is required')
            return False

        if authorService.getAuthorById(self.authorId) == None:
            self.addError('authorId', 'Author does not exist')
            return False

        if self.year == None:
            self.addError('year', 'Year is required')
            return False

        if ValidationHelper.parseInt(self.year) == False:
            self.addError('year', 'Year must be a valid number')
            return False

        if len(str(self.year)) > 5:
            self.addError('year', 'Year cannot be longer than 5 characters')
            return False

        if self.country == None or len(self.country) == 0:
            self.addError('country', 'Country is required')
            return False

        if len(self.country) > 50:
            self.addError('country', 'Country cannot be longer than 50 characters')
            return False

        if self.language == None or len(self.language) == 0:
            self.addError('language', 'Language is required')
            return False

        if len(self.language) > 50:
            self.addError('language', 'Language cannot be longer than 50 characters')
            return False

        if self.pages == None:
            self.addError('pages', 'Pages is required')
            return False

        if ValidationHelper.parseInt(self.pages) == False:
            self.addError('pages', 'Pages must be a valid number')
            return False

        return True

    def getAuthor(self):
        authorService = App.instance.getService('authors')

        # Get author from database
        author = authorService.getAuthorById(self.authorId)

        if author == None:
            raise Exception('Author with id ' + self.authorId + ' does not exist')

        return author

    def __str__(self):
        id = str(self.id)
        title = str(self.title)
        authorId = str(self.authorId)
        year = str(self.year)
        country = str(self.country)
        language = str(self.language)
        pages = str(self.pages)

        return id + ' - ' + title + ' - ' + authorId + ' - ' + year + ' - ' + country + ' - ' + language + ' - ' + pages

    @staticmethod
    def fromDataRow(row):
        return Book({
            'id': row[0],
            'title': row[1],
            'authorId': row[2],
            'year': row[3],
            'country': row[4],
            'language': row[5],
            'pages': row[6]
        })