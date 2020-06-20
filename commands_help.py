from base_app import App
from base_command import Command

class CommandHelp(Command):

    def getUsage(self):
        return 'help'

    def execute(self, args):
        commandService = App.instance.getService('commands')

        self.showEmpty()
        self.showInfo('Available commands:')
        self.showLine()

        # Prints the usage of all commands
        for command in commandService.commands.values():
            self.showInfo(command.getUsage())

        self.showEmpty()