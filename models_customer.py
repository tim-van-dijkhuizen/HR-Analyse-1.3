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
            self.addError('firstName', 'Voornaam mag niet leeg zijn')
            return False

        if self.lastName == None:
            self.addError('lastName', 'Achternaam mag niet leeg zijn')
            return False

        if self.gender == None:
            self.addError('gender', 'Geslacht mag niet leeg zijn')
            return False

        if self.language == None:
            self.addError('language', 'Taal mag niet leeg zijn')
            return False

        if self.street == None:
            self.addError('street', 'Straat mag niet leeg zijn')
            return False

        if self.zipcode == None:
            self.addError('zipcode', 'Postcode mag niet leeg zijn')
            return False

        if self.city == None:
            self.addError('city', 'Stad mag niet leeg zijn')
            return False

        if self.email == None:
            self.addError('email', 'Email mag niet leeg zijn')
            return False

        if self.telephone == None:
            self.addError('telephone', 'Telefoonnummer mag niet leeg zijn')
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