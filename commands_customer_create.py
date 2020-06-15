from base_command import Command
from errors_argument_exception import ArgumentError
from helpers_validation_helper import ValidationHelper
from models_customer import Customer

class CommandCustomerCreate(Command):

    def getUsage(self):
        return 'customer/create <firstName> <lastName> <gender> <language> <street> <zipcode> <city> <email> <telephone>'

    def execute(self, app, args):
        customerService = app.getService('customers')

        # Get arguments
        firstName = self.askQuestion('Enter the first name:')
        lastName = self.askQuestion('Enter the last name:')
        gender = self.askQuestion('Enter the gender:')
        language = self.askQuestion('Enter the language:')
        street = self.askQuestion('Enter the street:')
        zipcode = self.askQuestion('Enter the zipcode:')
        city = self.askQuestion('Enter the city:')
        email = self.askQuestion('Enter the email:')
        telephone = self.askQuestion('Enter the telephone:')

        # Create customer
        customer = Customer({
            'firstName': firstName,
            'lastName': lastName,
            'gender': gender,
            'language': language,
            'street': street,
            'zipcode': zipcode,
            'city': city,
            'email': email,
            'telephone': telephone
        })

    	# Save customer
        if customerService.saveCustomer(customer):
            print('Successfully saved customer')
        else:
            ValidationHelper.printErrorList(customer)