from base_command import Command

class CommandCustomerList(Command):

    def getUsage(self):
        return 'customer/list'

    def execute(self, app, args):
        customerService = app.getService('customers')

        self.showEmpty()
        self.showInfo('id - firstName - lastName - gender - language - street - zipcode - city - email - telephone')
        self.showLine()

        for customer in customerService.getCustomers():
            self.showInfo(customer)

        self.showEmpty()