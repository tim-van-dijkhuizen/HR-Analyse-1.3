from base_app import App
from base_command import Command

class CommandBackupRestore(Command):

    def getUsage(self):
        return 'backup/restore'

    def execute(self, args):
        database = App.instance.getService('database')

        # Ask for the backup
        backup = self.askQuestion('What backup do you want to restore?')

        # Try to restore the backup
        database.restoreBackup(backup)
        self.showInfo('Successfully restored backup ' + backup)