import sqlite3
from base_service import Service
from errors_argument_exception import ArgumentError
from helpers_file_helper import FileHelper

class DatabaseService(Service):

    # Constants
    backupFolder = 'backups/'

    _databasePath = None
    _connection = None

    def getHandle(self): 
        return 'database'

    def init(self):
        self._databasePath = FileHelper.createFilePath('PLS.db')
        FileHelper.createParentDirectories(self._databasePath)

        # Create connection
        self.connect()

        # Create cursor
        cursor = self.createCursor()

        # Enable foreign keys
        cursor.execute('PRAGMA foreign_keys=ON')

        # Create tables if not exists
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
            "year INTEGER(5) NOT NULL," +
            "country VARCHAR(50) NOT NULL," +
            "language VARCHAR(50) NOT NULL," +
            "pages INTEGER NOT NULL," +
            "FOREIGN KEY(authorId) REFERENCES authors(id) ON DELETE CASCADE" +
        ")")

        cursor.execute("CREATE TABLE IF NOT EXISTS book_items (" +
            "id INTEGER PRIMARY KEY," +
            "bookId INTEGER NOT NULL," +
            "FOREIGN KEY(bookId) REFERENCES books(id) ON DELETE CASCADE" +
        ")")

        cursor.execute("CREATE TABLE IF NOT EXISTS book_loans (" +
            "id INTEGER PRIMARY KEY," +
            "bookItemId INTEGER NOT NULL," +
            "customerId INTEGER NOT NULL," +
            "FOREIGN KEY(bookItemId) REFERENCES book_items(id) ON DELETE CASCADE," +
            "FOREIGN KEY(customerId) REFERENCES customers(id) ON DELETE CASCADE" +
        ")")
        
        self._connection.commit()

    # Creates a connection
    def connect(self):
        if self._connection != None:
            raise Exception('Database already connected')

        self._connection = sqlite3.connect(self._databasePath)

    # Disconnect
    def disconnect(self):
        if self._connection == None:
            raise Exception('Database already disconnected')

        self._connection.close()
        self._connection = None

    # Returns the database connection
    def getConnection(self):
        return self._connection

    # Creates a new cursor
    def createCursor(self):
        return self._connection.cursor()

    # Returns all backup names
    def getBackups(self):
        return FileHelper.listFiles(self._getBackupDirectory())

    # Creates a backup
    def createBackup(self, fileName):
        dest = self._getBackupPath(fileName)

        # Make sure the file doesn't exist
        if dest.exists():
            raise ArgumentError('A backup with that name already exists')

        # Copy DB to dest
        FileHelper.copyFile(self._databasePath, dest)

        return dest

    # Restores a backup
    def restoreBackup(self, fileName):
        backup = self._getBackupPath(fileName)

        # Make sure the file exist
        if not backup.exists():
            raise ArgumentError('That backup does not exist')

        # Close connection
        self.disconnect()

        # Copy backup to DB
        FileHelper.copyFile(backup, self._databasePath)

        # Reconnect
        self.connect()

    # Returns the backup directory path
    def _getBackupDirectory(self):
        return FileHelper.createFilePath(self.backupFolder)

    # Returns the backup path of a file
    def _getBackupPath(self, fileName):
        return FileHelper.createFilePath(self.backupFolder + fileName + '.db')

