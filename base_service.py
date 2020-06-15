from base_component import Component

class Service(Component):

    # Main app object
    app = None

    # Optional functions
    # ==========================================================
    
    def getHandle(self):
        raise NotImplementedError
    
    # Called after the service has been loaded
    def init(self): pass
    
