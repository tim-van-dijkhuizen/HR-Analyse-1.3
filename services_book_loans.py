from base_service import Service
from models_book_loan import BookLoan

class BookLoanService(Service):

    def getHandle(self): 
        return 'bookLoans'

    def getBookLoans(self):
        models = []

        # Create cursor
        cursor = self.app.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_loans')

        for row in cursor.fetchall():
            models.append(BookLoan.fromDataRow(row))

        return models

    def getBookLoanById(self, bookLoanId):
        cursor = self.app.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_loans WHERE id=?', [ bookLoanId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return BookLoan.fromDataRow(row)

    def getBookLoanByItem(self, bookItemId):
        cursor = self.app.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from book_loans WHERE bookItemId=?', [ bookItemId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return BookLoan.fromDataRow(row)

    def saveBookLoan(self, bookLoan):
        isNew = bookLoan.id == None

        # Validate model
        if not bookLoan.validate():
            return False

        database = self.app.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        sqlArgs = [
            bookLoan.bookItemId,
            bookLoan.customerId
        ]

        # Insert or update
        if isNew:
            cursor.execute("INSERT INTO book_loans (bookItemId, customerId) VALUES (?, ?);", sqlArgs)
        else:
            sqlArgs = sqlArgs + [ bookLoan.id ]
            cursor.execute("UPDATE book_loans SET bookItemId=?, customerId=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    def deleteBookLoan(self, bookLoan):
        database = self.app.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM book_loans WHERE id=?", [ bookLoan.id ])
        connection.commit()

        return cursor.rowcount != 0

