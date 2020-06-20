from base_app import App
from base_model import Model
from helpers_validation_helper import ValidationHelper

class BookLoan(Model):

    bookItemId = None
    customerId = None

    def validate(self):
        bookItemService = App.instance.getService('bookItems')
        customerService = App.instance.getService('customers')
        bookLoanService = App.instance.getService('bookLoans')

        # Validate relations
        if self.bookItemId == None:
            self.addError('bookItemId', 'Book item is required')
            return False

        if bookItemService.getBookItemById(self.bookItemId) == None:
            self.addError('bookItemId', 'Book item does not exist')
            return False

        if self.customerId == None:
            self.addError('customerId', 'Customer is required')
            return False

        if customerService.getCustomerById(self.customerId) == None:
            self.addError('customerId', 'Customer does not exist')
            return False

        if bookLoanService.getBookLoanByItem(self.bookItemId) != None:
            self.addError('bookItemId', 'Book item is not available')
            return False

        return True

    def getBookItem(self):
        bookItemService = App.instance.getService('bookItems')

        # Get book from database
        bookItem = bookItemService.getBookItemById(self.bookItemId)

        if bookItem == None:
            raise Exception('Book item with id ' + self.bookItemId + ' does not exist')

        return bookItem

    def getCustomer(self):
        customerService = App.instance.getService('customers')

        # Get customer from database
        customer = customerService.getCustomerById(self.customerId)

        if customer == None:
            raise Exception('Customer with id ' + self.customerId + ' does not exist')

        return customer

    def __str__(self):
        id = str(self.id)
        bookItemId = str(self.bookItemId)
        customerId = str(self.customerId)

        return id + ' - ' + bookItemId + ' - ' + customerId

    @staticmethod
    def fromDataRow(row):
        return BookLoan({
            'id': row[0],
            'bookItemId': row[1],
            'customerId': row[2]
        })