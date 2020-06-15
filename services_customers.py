from base_service import Service
from models_customer import Customer

class CustomersService(Service):

    def getHandle(self): 
        return 'customers'

    def getCustomers(self):
        models = []

        # Get database
        connection = self.app.getService('database').getConnection()
        cursor = connection.cursor()

        # Execute select
        cursor.execute('SELECT * from customers')

        for row in cursor.fetchall():
            models.append(Customer({
                'firstName': row[0],
                'lastName': row[1],
                'gender': row[2],
                'language': row[3],
                'street': row[4],
                'zipcode': row[5],
                'city': row[6],
                'email': row[7],
                'telephone': row[8]
            }))

        return models

    def saveCustomer(self, customer):
        isNew = customer.id == None

        # Validate model
        if not customer.validate():
            return False

        connection = self.app.getService('database').getConnection()
        cursor = connection.cursor()

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
        else:
            sqlArgs = sqlArgs.append(customer.id)
            cursor.execute("UPDATE customers SET firstName=?, lastName=?, gender=?, language=?, street=?, zipcode=?, city=?, email=?, telephone=? WHERE id=?;", sqlArgs)

        connection.commit()
        return True

