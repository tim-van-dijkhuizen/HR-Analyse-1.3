from base_app import App
from base_command import Command

class CommandBackupList(Command):

    def getUsage(self):
        return 'backup/list'

    def execute(self, args):
        database = App.instance.getService('database')

        self.showEmpty()
        self.showInfo('Backup filenames')
        self.showLine()

        # Get backups
        backups = database.getBackups()

        # Show message when there are no results
        if not backups:
            self.showError('No backups found')

        for backup in backups:
            self.showInfo(str(backup).replace('.db', ''))

        self.showEmpty()