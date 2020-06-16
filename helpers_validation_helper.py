class ValidationHelper:

    @staticmethod
    def printErrorList(model):
        print('Validation errors:')

        for attribute, errors in model.getErrors().items():
            for error in errors:
                print(attribute, ' -> ', error)

    @staticmethod
    def parseInt(value):
        try: 
            return int(value)
        except ValueError:
            return False