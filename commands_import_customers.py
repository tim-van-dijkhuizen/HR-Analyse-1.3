import csv
from base_app import App
from base_command import Command
from helpers_file_helper import FileHelper
from helpers_validation_helper import ValidationHelper
from models_customer import Customer

class CommandImportCustomers(Command):

    def getUsage(self):
        return 'import/customers'

    def execute(self, args):
        customerService = App.instance.getService('customers')

        # Get json from file
        rawPath = self.askQuestion('Which file would you like to import?')
        filePath = FileHelper.createFilePath(rawPath, True)

        if not filePath.exists():
            self.showError('Csv file doesn\'t exist')

        try:
            fileContent = open(filePath, encoding = 'utf8')
            data = csv.reader(fileContent)
        except csv.Error:
            self.showError('Failed to load csv. The file contains invalid data.')
        except Exception:
            self.showError('Failed to load csv. Unable to read file contents.')

        # Skip CSV header
        next(data, None)

        # Create customers
        for customerRow in data:
            self._validateCsvRow(customerRow)

            # Create customer
            customer = Customer({
                'firstName': customerRow[3],
                'lastName': customerRow[4],
                'gender': 'M' if customerRow[1] == 'male' else 'F',
                'language': customerRow[2],
                'street': customerRow[5],
                'zipcode': customerRow[6],
                'city': customerRow[7],
                'email': customerRow[8],
                'telephone': customerRow[10]
            })

            # Try to save
            if not customerService.saveCustomer(customer):
                ValidationHelper.printErrorList(customer)
                raise Exception('Unable to save customer: ' + customerRow['title'])

        # Close file
        fileContent.close()

        self.showInfo('Successfully imported customers')

    def _validateCsvRow(self, row):
        if len(row) != 11:
            self.showError('All rows must have 11 columns')
