from base_app import App
from base_command import Command
from helpers_validation_helper import ValidationHelper
from models_author import Author

class CommandAuthorCreate(Command):

    def getUsage(self):
        return 'author/create'

    def execute(self, args):
        authorService = App.instance.getService('authors')

        # Get arguments
        firstName = self.askQuestion('Enter the first name:')
        lastName = self.askQuestion('Enter the last name:')

        # Create author
        author = Author({
            'firstName': firstName,
            'lastName': lastName
        })

    	# Try to save
        if authorService.saveAuthor(author):
            self.showInfo('Successfully created author')
        else:
            ValidationHelper.printErrorList(author)