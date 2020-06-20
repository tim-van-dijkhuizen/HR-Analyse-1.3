import datetime
from base_app import App
from base_command import Command

class CommandBackupCreate(Command):

    def getUsage(self):
        return 'backup/create'

    def execute(self, args):
        database = App.instance.getService('database')

        # Ask for the filename
        defaultFileName = 'backup_{0:%d-%m-%Y_%H-%M-%S}'.format(datetime.datetime.now())
        fileName = self.askQuestion('What should be the name of the backup?', defaultFileName)

        # Try to create the backup
        backupDest = database.createBackup(fileName)
        self.showInfo('Successfully created backup at: ' + str(backupDest))