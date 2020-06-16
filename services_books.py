from base_service import Service
from models_book import Book

class BookService(Service):

    def getHandle(self): 
        return 'books'

    def getBooks(self):
        models = []

        # Create cursor
        cursor = self.app.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from books')

        for row in cursor.fetchall():
            models.append(Book.fromDataRow(row))

        return models

    def getBookById(self, bookId):
        cursor = self.app.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from books WHERE id=?', [ bookId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return Book.fromDataRow(row)

    def saveBook(self, book):
        isNew = book.id == None

        # Validate model
        if not book.validate():
            return False

        database = self.app.getService('database')
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
        else:
            sqlArgs = sqlArgs + [ book.id ]
            cursor.execute("UPDATE books SET title=?, authorId=?, year=?, country=?, language=?, pages=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    def deleteBook(self, book):
        database = self.app.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM books WHERE id=?", [ book.id ])
        connection.commit()

        return cursor.rowcount != 0

