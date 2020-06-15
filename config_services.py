from services_database import DatabaseService
from services_customers import CustomersService
from services_commands import CommandsService
from commands_stop import CommandStop
from commands_customer_list import CommandCustomerList
from commands_customer_create import CommandCustomerCreate

services = [
    [ DatabaseService, {  } ],

    [ CustomersService, {} ],

    [ CommandsService, { 'commands': {
        'stop': CommandStop(),
        'customer/list': CommandCustomerList(),
        'customer/create': CommandCustomerCreate()
    } } ]
]
