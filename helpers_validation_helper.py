class ValidationHelper:

    # Prints all validation errors of the specified model
    @staticmethod
    def printErrorList(model):
        print('Validation errors:')

        for attribute, errors in model.getErrors().items():
            for error in errors:
                print(attribute, ' -> ', error)

    # Parses a value to int or returns false on failure
    @staticmethod
    def parseInt(value):
        try: 
            return int(value)
        except ValueError:
            return False