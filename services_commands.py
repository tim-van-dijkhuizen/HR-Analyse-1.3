from base_app import App
import traceback
from base_service import Service
from errors_argument_exception import ArgumentError

class CommandService(Service):

    commands = []

    def getHandle(self):
        return 'commands'

    def init(self):
        # Keep running until the app is shut down
        while App.instance.running:
            line = input()
            args = line.split(' ')
            command = args.pop(0)

            # Try to run the command if it exists
            if command in self.commands:
                try:
                    self.commands[command].execute(args)
                except ArgumentError as e:
                    print(str(e))
                except Exception as e:
                    traceback.print_exc()
            else:
                print('Unknown command')