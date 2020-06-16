from base_command import Command

class CommandBookList(Command):

    def getUsage(self):
        return 'book/list'

    def execute(self, app, args):
        bookService = app.getService('books')

        self.showEmpty()
        self.showInfo('id - title - authorId - year - country - language - pages')
        self.showLine()

        for book in bookService.getBooks():
            self.showInfo(book)

        self.showEmpty()