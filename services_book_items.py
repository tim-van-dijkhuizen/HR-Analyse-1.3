from base_app import App
from base_service import Service
from models_book_item import BookItem

class BookItemService(Service):

    def getHandle(self): 
        return 'bookItems'

    # Returns all book items
    def getBookItems(self):
        models = []

        # Create cursor
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_items')

        for row in cursor.fetchall():
            models.append(BookItem.fromDataRow(row))

        return models

    # Returns a book item by its id or None
    def getBookItemById(self, bookItemId):
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_items WHERE id=?', [ bookItemId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return BookItem.fromDataRow(row)

    # Returns all book items by bookId
    def getBookItemsByBook(self, bookId):
        models = []

        # Create cursor
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_items WHERE bookId=?', [ bookId ])

        for row in cursor.fetchall():
            models.append(BookItem.fromDataRow(row))

        return models

    # Saves a book item
    def saveBookItem(self, bookItem):
        isNew = bookItem.id == None

        # Validate model
        if not bookItem.validate():
            return False

        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        sqlArgs = [
            bookItem.bookId
        ]

        # Insert or update
        if isNew:
            cursor.execute("INSERT INTO book_items (bookId) VALUES (?);", sqlArgs)
            bookItem.id = cursor.lastrowid
        else:
            sqlArgs = sqlArgs + [ bookItem.id ]
            cursor.execute("UPDATE book_items SET bookId=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    # Deletes a book item
    def deleteBookItem(self, bookItem):
        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM book_items WHERE id=?", [ bookItem.id ])
        connection.commit()

        return cursor.rowcount != 0

