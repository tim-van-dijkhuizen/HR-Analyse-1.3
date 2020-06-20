import time
from base_app import App
from base_component import Component
from errors_argument_exception import ArgumentError

class Command(Component):

    # Returns the command usage info
    def getUsage(self):
        raise NotImplementedError()

    # Executes the command code
    def execute(self, args):
        raise NotImplementedError()

    # Prints an empty line
    def showEmpty(self):
        print()

    # Prints a line
    def showLine(self):
        print('-------------------------------------------------------------------------------------------')

    # Prints a message
    def showInfo(self, message):
        print(message)

    # Prints a message and stops code execution
    def showError(self, message):
        raise ArgumentError(message)

    # Shows an error with the usage info
    def showUsage(self):
        self.showError("Usage: " + self.getUsage())

    # Asks the user for input
    def askQuestion(self, question, defaultValue = None):
        print(self._getQuestionMessage(question, defaultValue))

        # Get answer
        answer = input()

        if defaultValue != None and len(answer) == 0:
            return defaultValue

        return answer

    # Builds the question message (internal)
    def _getQuestionMessage(self, question, defaultValue):
        message = question

        if defaultValue != None:
            message += " [" + str(defaultValue) + "]"

        return message