from base_app import App
from base_service import Service
from models_book_loan import BookLoan

class BookLoanService(Service):

    def getHandle(self): 
        return 'bookLoans'

    # Returns all book loans
    def getBookLoans(self):
        models = []

        # Create cursor
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_loans')

        for row in cursor.fetchall():
            models.append(BookLoan.fromDataRow(row))

        return models

    # Returns a book loan by its id or None
    def getBookLoanById(self, bookLoanId):
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_loans WHERE id=?', [ bookLoanId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return BookLoan.fromDataRow(row)

    # Returns a book loan by its itemId or None
    def getBookLoanByItem(self, bookItemId):
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_loans WHERE bookItemId=?', [ bookItemId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return BookLoan.fromDataRow(row)

    # Saves a book loan
    def saveBookLoan(self, bookLoan):
        isNew = bookLoan.id == None

        # Validate model
        if not bookLoan.validate():
            return False

        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        sqlArgs = [
            bookLoan.bookItemId,
            bookLoan.customerId
        ]

        # Insert or update
        if isNew:
            cursor.execute("INSERT INTO book_loans (bookItemId, customerId) VALUES (?, ?);", sqlArgs)
            bookLoan.id = cursor.lastrowid
        else:
            sqlArgs = sqlArgs + [ bookLoan.id ]
            cursor.execute("UPDATE book_loans SET bookItemId=?, customerId=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    # Deletes a book loan
    def deleteBookLoan(self, bookLoan):
        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM book_loans WHERE id=?", [ bookLoan.id ])
        connection.commit()

        return cursor.rowcount != 0

