from base_command import Command
from helpers_validation_helper import ValidationHelper

class CommandCustomerEdit(Command):

    def getUsage(self):
        return 'customer/edit <customerId>'

    def execute(self, app, args):
        customerService = app.getService('customers')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Get customer by id
        customer = customerService.getCustomerById(args[0])

        if customer == None:
            self.showError('Invalid customer')

        # Update customer
        customer.firstName = self.askQuestion('Enter the first name:', customer.firstName)
        customer.lastName = self.askQuestion('Enter the last name:', customer.lastName)
        customer.gender = self.askQuestion('Enter the gender:', customer.gender)
        customer.language = self.askQuestion('Enter the language:', customer.language)
        customer.street = self.askQuestion('Enter the street:', customer.street)
        customer.zipcode = self.askQuestion('Enter the zipcode:', customer.zipcode)
        customer.city = self.askQuestion('Enter the city:', customer.city)
        customer.email = self.askQuestion('Enter the email:', customer.email)
        customer.telephone = self.askQuestion('Enter the telephone:', customer.telephone)

    	# Try to save
        if customerService.saveCustomer(customer):
            self.showInfo('Successfully saved customer')
        else:
            ValidationHelper.printErrorList(customer)