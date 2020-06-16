import time
from base_app import App
from base_component import Component
from errors_argument_exception import ArgumentError

class Command(Component):

    def getUsage(self):
        raise NotImplementedError()

    def execute(self, app, args):
        raise NotImplementedError()

    def showEmpty(self):
        print()

    def showLine(self):
        print('-------------------------------------------------------------------------------------------')

    def showInfo(self, message):
        print(message)

    def showError(self, message):
        raise ArgumentError(message)

    def showUsage(self):
        self.showError("Usage: " + self.getUsage())

    def askQuestion(self, question, defaultValue = None):
        print(self._getQuestionMessage(question, defaultValue))

        # Get answer
        answer = input()

        if defaultValue != None and len(answer) == 0:
            return defaultValue

        return answer

    def _getQuestionMessage(self, question, defaultValue):
        message = question

        if defaultValue != None:
            message += " [" + str(defaultValue) + "]"

        return message