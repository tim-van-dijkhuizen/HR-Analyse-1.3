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

        # Get customers
        customers = customerService.getCustomers()

        # Show message when there are no results
        if not customers:
            self.showError('No customers found')

        for customer in customers:
            self.showInfo(customer)

        self.showEmpty()