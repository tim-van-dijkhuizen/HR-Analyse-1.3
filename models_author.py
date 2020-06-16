from base_model import Model

class Author(Model):

    firstName = None
    lastName = None

    def validate(self):
        if self.firstName == None:
            self.addError('firstName', 'Voornaam mag niet leeg zijn')
            return False

        if self.lastName == None:
            self.addError('lastName', 'Achternaam mag niet leeg zijn')
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