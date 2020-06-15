from base_command import Command

class CommandCustomerList(Command):

    def getUsage(self):
        return 'customer/list'

    def execute(self, app, args):
        customerService = app.getService('customers')

        for customer in customerService.getCustomers():
            print(customer)