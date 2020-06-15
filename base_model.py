from base_component import Component

class Model(Component):

    # List of validation errors
    errors = {}

    # Validates the model
    def validate(self):
        return True

    # Adds an error to this model
    def addError(self, attribute, error):
        errors = self.getErrors(attribute)

        # Add error if not present already
        if not (error in errors):
            errors.append(error)

    # Returns all errors for the specified attribute
    def getErrors(self, attribute = None):
        if attribute == None:
            return self.errors

        if not (attribute in self.errors):
            self.errors[attribute] = []

        return self.errors[attribute]

    # Returns whether this model has valiation errors
    def hasErrors(self):
        return len(self.errors) > 0