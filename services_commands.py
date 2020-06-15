from base_service import Service
from errors_argument_exception import ArgumentError

class CommandsService(Service):

    commands = []

    def getHandle(self):
        return 'commands'

    def init(self):
        while self.app.running:
            line = input()
            args = line.split(' ')
            command = args.pop(0)

            # Execute command on new thread
            if command in self.commands:
                try:
                    self.commands[command].execute(self.app, args)
                except ArgumentError as e:
                    print(str(e))
                except Exception as e:
                    print('An internal error occurred: ' + str(e))
            else:
                print('Unknown command')