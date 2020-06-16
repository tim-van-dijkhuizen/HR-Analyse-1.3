from base_command import Command
from helpers_validation_helper import ValidationHelper

class CommandAuthorEdit(Command):

    def getUsage(self):
        return 'author/edit <authorId>'

    def execute(self, app, args):
        authorService = app.getService('authors')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Get author by id
        author = authorService.getAuthorById(args[0])

        if author == None:
            self.showError('Invalid author')

        # Update author
        author.firstName = self.askQuestion('Enter the first name:', author.firstName)
        author.lastName = self.askQuestion('Enter the last name:', author.lastName)

    	# Try to save
        if authorService.saveAuthor(author):
            self.showInfo('Successfully saved author')
        else:
            ValidationHelper.printErrorList(author)