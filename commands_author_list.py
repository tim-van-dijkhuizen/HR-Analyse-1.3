from base_command import Command

class CommandAuthorList(Command):

    def getUsage(self):
        return 'author/list'

    def execute(self, app, args):
        authorService = app.getService('authors')

        self.showEmpty()
        self.showInfo('id - firstName - lastName')
        self.showLine()

        for author in authorService.getAuthors():
            self.showInfo(author)

        self.showEmpty()