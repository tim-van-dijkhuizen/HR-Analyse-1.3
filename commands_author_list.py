from base_app import App
from base_command import Command

class CommandAuthorList(Command):

    def getUsage(self):
        return 'author/list'

    def execute(self, args):
        authorService = App.instance.getService('authors')

        self.showEmpty()
        self.showInfo('id - firstName - lastName')
        self.showLine()

        # Get authors
        authors = authorService.getAuthors()

        # Show message when there are no results
        if not authors:
            self.showError('No authors found')

        for author in authors:
            self.showInfo(author)

        self.showEmpty()