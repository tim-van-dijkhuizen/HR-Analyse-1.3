from base_app import App
from base_service import Service
from models_author import Author

class AuthorService(Service):

    def getHandle(self): 
        return 'authors'

    def getAuthors(self):
        models = []

        # Create cursor
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from authors')

        for row in cursor.fetchall():
            models.append(Author.fromDataRow(row))

        return models

    def getAuthorById(self, authorId):
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from authors WHERE id=?', [ authorId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return Author.fromDataRow(row)

    def saveAuthor(self, author):
        isNew = author.id == None

        # Validate model
        if not author.validate():
            return False

        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        sqlArgs = [
            author.firstName,
            author.lastName
        ]

        # Insert or update
        if isNew:
            cursor.execute("INSERT INTO authors (firstName, lastName) VALUES (?, ?);", sqlArgs)
            author.id = cursor.lastrowid
        else:
            sqlArgs = sqlArgs + [ author.id ]
            cursor.execute("UPDATE authors SET firstName=?, lastName=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    def deleteAuthor(self, author):
        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM authors WHERE id=?", [ author.id ])
        connection.commit()

        return cursor.rowcount != 0

