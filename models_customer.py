from models_person import Person

class Customer(Person):

    id = None
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
        firstName = str(self.firstName)
        lastName = str(self.lastName)
        gender = str(self.gender)
        language = str(self.language)
        street = str(self.street)
        zipcode = str(self.zipcode)
        city = str(self.city)
        email = str(self.email)
        telephone = str(self.telephone)

        return firstName + ' - ' + lastName + ' - ' + gender + ' - ' + language + ' - ' + street + ' - ' + zipcode + ' - ' + city + ' - ' + email + ' - ' + telephone