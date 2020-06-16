from base_command import Command

class CommandHelp(Command):

    def getUsage(self):
        return 'help'

    def execute(self, app, args):
        commandService = app.getService('commands')

        self.showEmpty()
        self.showInfo('Available commands:')
        self.showLine()

        for command in commandService.commands.values():
            self.showInfo(command.getUsage())

        self.showEmpty()