from base_app import App
from base_service import Service
from models_customer import Customer

class CustomerService(Service):

    def getHandle(self): 
        return 'customers'

    def getCustomers(self):
        models = []

        # Create cursor
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from customers')

        for row in cursor.fetchall():
            models.append(Customer.fromDataRow(row))

        return models

    def getCustomerById(self, customerId):
        cursor = App.instance.getService('database').createCursor()

        # Execute select
        cursor.execute('SELECT * from customers WHERE id=?', [ customerId ])

        # Parse result
        row = cursor.fetchone()

        if row == None:
            return None

        return Customer.fromDataRow(row)

    def saveCustomer(self, customer):
        isNew = customer.id == None

        # Validate model
        if not customer.validate():
            return False

        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        sqlArgs = [
            customer.firstName,
            customer.lastName,
            customer.gender,
            customer.language,
            customer.street,
            customer.zipcode,
            customer.city,
            customer.email,
            customer.telephone
        ]

        # Insert or update
        if isNew:
            cursor.execute("INSERT INTO customers (firstName, lastName, gender, language, street, zipcode, city, email, telephone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", sqlArgs)
            customer.id = cursor.lastrowid
        else:
            sqlArgs = sqlArgs + [ customer.id ]
            cursor.execute("UPDATE customers SET firstName=?, lastName=?, gender=?, language=?, street=?, zipcode=?, city=?, email=?, telephone=? WHERE id=?;", sqlArgs)

        connection.commit()

        return cursor.rowcount != 0

    def deleteCustomer(self, customer):
        database = App.instance.getService('database')
        connection = database.getConnection()
        cursor = database.createCursor()

        # Delete from database
        cursor.execute("DELETE FROM customers WHERE id=?", [ customer.id ])
        connection.commit()

        return cursor.rowcount != 0

