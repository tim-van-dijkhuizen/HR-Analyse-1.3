from base_command import Command

class CommandStop(Command):

    def execute(self, app, args):
        print('Stopping app...')
        app.running = False