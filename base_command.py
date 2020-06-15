import time
from base_app import App
from base_component import Component
from base_question import Question
from errors_argument_exception import ArgumentError

class Command(Component):

    def getUsage(self):
        raise NotImplementedError()

    def execute(self, app, args):
        raise NotImplementedError()

    def showUsage(self):
        raise ArgumentError("Usage: " + self.getUsage())

    def askQuestion(self, question):
        print(question)
        return input()