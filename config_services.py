from services_database import DatabaseService
from services_customers import CustomersService
from services_commands import CommandsService
from commands_help import CommandHelp
from commands_stop import CommandStop
from commands_customer_list import CommandCustomerList
from commands_customer_create import CommandCustomerCreate
from commands_customer_edit import CommandCustomerEdit
from commands_customer_delete import CommandCustomerDelete

services = [
    [ DatabaseService, {  } ],

    [ CustomersService, {} ],

    [ CommandsService, { 'commands': {
        'help': CommandHelp(),
        'stop': CommandStop(),
        'customer/list': CommandCustomerList(),
        'customer/create': CommandCustomerCreate(),
        'customer/edit': CommandCustomerEdit(),
        'customer/delete': CommandCustomerDelete()
    } } ]
]
