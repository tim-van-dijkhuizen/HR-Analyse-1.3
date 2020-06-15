class ValidationHelper:

    @staticmethod
    def printErrorList(model):
        for attribute, errors in model.getErrors():
            for error in errors:
                print(attribute, ' -> ', error)