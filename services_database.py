import sqlite3
from base_service import Service

class DatabaseService(Service):

    _connection = None

    def getHandle(self): 
        return 'database'

    def init(self):
        self._connection = sqlite3.connect('PLS.db')

        # Create tables if not exists
        cursor = self._connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS customers (" +
            "id INTEGER PRIMARY KEY," +
            "firstName VARCHAR(50) NOT NULL," +
            "lastName VARCHAR(50) NOT NULL," +
            "gender VARCHAR(1) NOT NULL," +
            "language VARCHAR(50) NOT NULL," +
            "street VARCHAR(50) NOT NULL," +
            "zipcode VARCHAR(20) NOT NULL," +
            "city VARCHAR(50) NOT NULL," +
            "email VARCHAR(255) NOT NULL," +
            "telephone VARCHAR(255) NOT NULL" +
        ")")

        cursor.execute("CREATE TABLE IF NOT EXISTS authors (" +
            "id integer PRIMARY KEY," +
            "firstName VARCHAR(50) NOT NULL," +
            "lastName VARCHAR(50) NOT NULL" +
        ")")

        cursor.execute("CREATE TABLE IF NOT EXISTS books (" +
            "id INTEGER PRIMARY KEY," +
            "title VARCHAR(255) NOT NULL," +
            "authorId INTEGER NOT NULL," +
            "year INTEGER(4) NOT NULL," +
            "country VARCHAR(50) NOT NULL," +
            "language VARCHAR(50) NOT NULL," +
            "pages INTEGER NOT NULL," +
            "FOREIGN KEY(authorId) REFERENCES authors(id)" +
        ")")

        cursor.execute("CREATE TABLE IF NOT EXISTS book_items (" +
            "id INTEGER PRIMARY KEY," +
            "bookId INTEGER NOT NULL," +
            "FOREIGN KEY(bookId) REFERENCES books(id)" +
        ")")

        cursor.execute("CREATE TABLE IF NOT EXISTS book_loans (" +
            "id INTEGER PRIMARY KEY," +
            "bookItemId INTEGER NOT NULL," +
            "customerId INTEGER NOT NULL," +
            "FOREIGN KEY(bookItemId) REFERENCES book_items(id)," +
            "FOREIGN KEY(customerId) REFERENCES customers(id)" +
        ")")
        
        self._connection.commit()

    def getConnection(self):
        return self._connection

    def createCursor(self):
        return self._connection.cursor()
