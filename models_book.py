from base_app import App
from base_model import Model

class Book(Model):

    title = None
    authorId = None
    year = None
    country = None
    language = None
    pages = None

    def validate(self):
        if self.title == None:
            self.addError('title', 'Title is required')
            return False

        if self.authorId == None:
            self.addError('authorId', 'Author is required')
            return False

        if self.year == None:
            self.addError('year', 'Year is required')
            return False

        if self.country == None:
            self.addError('country', 'Country is required')
            return False

        if self.language == None:
            self.addError('language', 'Language is required')
            return False

        if self.pages == None:
            self.addError('pages', 'Pages is required')
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