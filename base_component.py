class Component:

    # Sets all attributes from the config
    # and calls setup().
    def __init__(self, config = {}):
        for attribute, value in config.items():
            setattr(self, attribute, value)
    
        self.setup()

    # Returns the name of this class
    def getClassName(self):
        return self.__class__.__name__

    # Called on setup
    def setup(self): pass
