from base_model import Model

class Customer(Model):

    firstName = None
    lastName = None
    gender = None
    language = None
    street = None
    zipcode = None
    city = None
    email = None
    telephone = None

    def validate(self):
        if self.firstName == None:
            self.addError('firstName', 'Firstname is required')
            return False

        if len(self.firstName) > 50:
            self.addError('firstName', 'Firstname cannot be longer than 50 characters')
            return False

        if self.lastName == None:
            self.addError('lastName', 'Lastname is required')
            return False

        if len(self.lastName) > 50:
            self.addError('lastName', 'Lastname cannot be longer than 50 characters')
            return False

        if self.gender != 'M' and self.gender != 'F':
            self.addError('gender', 'Gender must be either M (male) or F (female)')
            return False

        if self.language == None:
            self.addError('language', 'Language is required')
            return False

        if len(self.language) > 50:
            self.addError('language', 'Language cannot be longer than 50 characters')
            return False

        if self.street == None:
            self.addError('street', 'Street is required')
            return False

        if len(self.street) > 50:
            self.addError('street', 'Street cannot be longer than 50 characters')
            return False

        if self.zipcode == None:
            self.addError('zipcode', 'Zipcode is required')
            return False

        if len(self.zipcode) > 20:
            self.addError('zipcode', 'Zipcode cannot be longer than 20 characters')
            return False

        if self.city == None:
            self.addError('city', 'City is required')
            return False

        if len(self.city) > 50:
            self.addError('city', 'City cannot be longer than 50 characters')
            return False

        if self.email == None:
            self.addError('email', 'Email is required')
            return False

        if len(self.email) > 255:
            self.addError('email', 'Email cannot be longer than 255 characters')
            return False

        if self.telephone == None:
            self.addError('telephone', 'Telephone is required')
            return False

        if len(self.telephone) > 255:
            self.addError('telephone', 'Telephone cannot be longer than 255 characters')
            return False

        return True

    def __str__(self):
        id = str(self.id)
        firstName = str(self.firstName)
        lastName = str(self.lastName)
        gender = str(self.gender)
        language = str(self.language)
        street = str(self.street)
        zipcode = str(self.zipcode)
        city = str(self.city)
        email = str(self.email)
        telephone = str(self.telephone)

        return id + ' - ' + firstName + ' - ' + lastName + ' - ' + gender + ' - ' + language + ' - ' + street + ' - ' + zipcode + ' - ' + city + ' - ' + email + ' - ' + telephone

    @staticmethod
    def fromDataRow(row):
        return Customer({
            'id': row[0],
            'firstName': row[1],
            'lastName': row[2],
            'gender': row[3],
            'language': row[4],
            'street': row[5],
            'zipcode': row[6],
            'city': row[7],
            'email': row[8],
            'telephone': row[9]
        })