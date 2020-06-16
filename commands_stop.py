from base_command import Command

class CommandStop(Command):

    def getUsage(self):
        return 'stop'

    def execute(self, app, args):
        print('Stopping app...')
        app.running = False