from base_app import App
from base_service import Service
from models_book import Book

class BookService(Service):

    def getHandle(self): 
        return 'books'

    # Returns all books
    def getBooks(self):
        models = []

        # Create cursor
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from books')

        for row in cursor.fetchall():
            models.append(Book.fromDataRow(row))

        return models

    # Returns a book by its id or None
    def getBookById(self, bookId):
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from books WHERE id=?', [ bookId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return Book.fromDataRow(row)

    # Returns all books matching the query
    def searchBooks(self, query):
        cursor = App.instance.getService('database').createCursor()
        models = []
        param = '%' + query + '%'

        # Execute select
        cursor.execute('SELECT * from books LEFT JOIN authors ON books.authorId = authors.id WHERE ' +
            'title LIKE ? ' +
            'OR authors.firstName || " " || authors.lastName LIKE ? ' +
            'OR year LIKE ? ' +
            'OR country LIKE ? ' +
            'OR language LIKE ? ' +
            'OR pages LIKE ?'
        , [ param, param, param, param, param, param ])

        # Parse result
        for row in cursor.fetchall():
            models.append(Book.fromDataRow(row))

        return models

    # Saves a book
    def saveBook(self, book):
        isNew = book.id == None

        # Validate model
        if not book.validate():
            return False

        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        sqlArgs = [
            book.title,
            book.authorId,
            book.year,
            book.country,
            book.language,
            book.pages
        ]

        # Insert or update
        if isNew:
            cursor.execute("INSERT INTO books (title, authorId, year, country, language, pages) VALUES (?, ?, ?, ?, ?, ?);", sqlArgs)
            book.id = cursor.lastrowid
        else:
            sqlArgs = sqlArgs + [ book.id ]
            cursor.execute("UPDATE books SET title=?, authorId=?, year=?, country=?, language=?, pages=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    # Deletes a book
    def deleteBook(self, book):
        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM books WHERE id=?", [ book.id ])
        connection.commit()

        return cursor.rowcount != 0

