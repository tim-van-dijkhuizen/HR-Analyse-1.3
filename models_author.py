from base_model import Model

class Author(Model):

    firstName = None
    lastName = None

    def validate(self):
        if self.firstName == None or len(self.firstName) == 0:
            self.addError('firstName', 'Firstname is required')
            return False

        if len(self.firstName) > 50:
            self.addError('firstName', 'Firstname cannot be longer than 50 characters')
            return False

        if len(self.lastName) > 50:
            self.addError('lastName', 'Lastname cannot be longer than 50 characters')
            return False

        return True

    def __str__(self):
        id = str(self.id)
        firstName = str(self.firstName)
        lastName = str(self.lastName)

        return id + ' - ' + firstName + ' - ' + lastName

    @staticmethod
    def fromDataRow(row):
        return Author({
            'id': row[0],
            'firstName': row[1],
            'lastName': row[2]
        })