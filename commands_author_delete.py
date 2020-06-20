from base_app import App
from base_command import Command

class CommandAuthorDelete(Command):

    def getUsage(self):
        return 'author/delete <authorId>'

    def execute(self, args):
        authorService = App.instance.getService('authors')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Find author
        author = authorService.getAuthorById(args[0])

        if author == None:
            self.showError('Invalid author')

        # Try to delete
        if authorService.deleteAuthor(author):
            self.showInfo('Successfully deleted author')
        else:
            self.showError('Failed to delete author')