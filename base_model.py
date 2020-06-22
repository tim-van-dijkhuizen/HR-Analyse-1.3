from base_component import Component

class Model(Component):

    id = None

    def __init__(self, config = {}):
        super(Model, self).__init__(config)
        self.errors = {}

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