from base_command import Command

class CommandCustomerDelete(Command):

    def getUsage(self):
        return 'customer/delete <customerId>'

    def execute(self, app, args):
        customerService = app.getService('customers')

        # Check args length
        if len(args) != 1:
            self.showUsage()

        # Find customer
        customer = customerService.getCustomerById(args[0])

        if customer == None:
            self.showError('Invalid customer')

        # Try to delete
        if customerService.deleteCustomer(customer):
            self.showInfo('Successfully deleted customer')
        else:
            self.showError('Failed to delete customer')