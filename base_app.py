from base_component import Component

class App(Component):
    
    # Globals
    # ==========================================================
    
    instance = None

    # All registered service objects
    serviceMap = {}
    
    # Whether the application is running
    running = True

    # Setup
    # ==========================================================

    def setup(self):
        App.instance = self

    # Functions
    # ==========================================================
    
    # Returns a Service by its handle
    def getService(self, handle):
        try:
            return self.serviceMap[handle]
        except KeyError:
            raise Exception('No service with handle ' + handle + ' exists')
    
    # Registers a service and returns the instance.
    def registerService(self, service, config):
        instance = service(config)

        # Register instance
        self.serviceMap[instance.getHandle()] = instance

        # Init service
        instance.init()
            
        return instance
