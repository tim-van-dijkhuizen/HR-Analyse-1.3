from base_app import App
from base_command import Command

class CommandStop(Command):

    def getUsage(self):
        return 'stop'

    def execute(self, args):
        print('Stopping app...')
        App.instance.running = False