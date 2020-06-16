from base_app import App
from config_services import services as serviceList

# Bootstrap
# ==========================================================

# Create app
app = App()

print('-------------------------------------------------------------------------------------------')
print('Welcome to Public Library System')
print('Use the "help" command to view all available commands')
print('-------------------------------------------------------------------------------------------')

# Register services inside App
for service in serviceList:
    app.registerService(service[0], service[1])