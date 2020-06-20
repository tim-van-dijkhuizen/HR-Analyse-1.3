from base_app import App
from base_command import Command

class CommandCustomerList(Command):

    def getUsage(self):
        return 'customer/list'

    def execute(self, args):
        customerService = App.instance.getService('customers')

        self.showEmpty()
        self.showInfo('id - firstName - lastName - gender - language - street - zipcode - city - email - telephone')
        self.showLine()

        for customer in customerService.getCustomers():
            self.showInfo(customer)

        self.showEmpty()