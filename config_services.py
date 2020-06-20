from services_database import DatabaseService

from services_customers import CustomerService
from services_authors import AuthorService
from services_books import BookService
from services_book_items import BookItemService
from services_book_loans import BookLoanService

from services_commands import CommandService
from commands_help import CommandHelp
from commands_stop import CommandStop
from commands_customer_list import CommandCustomerList
from commands_customer_create import CommandCustomerCreate
from commands_customer_edit import CommandCustomerEdit
from commands_customer_delete import CommandCustomerDelete
from commands_author_list import CommandAuthorList
from commands_author_create import CommandAuthorCreate
from commands_author_edit import CommandAuthorEdit
from commands_author_delete import CommandAuthorDelete
from commands_book_list import CommandBookList
from commands_book_search import CommandBookSearch
from commands_book_create import CommandBookCreate
from commands_book_edit import CommandBookEdit
from commands_book_delete import CommandBookDelete
from commands_book_item_list import CommandBookItemList
from commands_book_item_create import CommandBookItemCreate
from commands_book_item_delete import CommandBookItemDelete
from commands_book_loan_list import CommandBookLoanList
from commands_book_loan_create import CommandBookLoanCreate
from commands_book_loan_delete import CommandBookLoanDelete

# =======================================================
# This file is used to register all services.
# You can pass a dictionary to configure the service.
# =======================================================

services = [
    [ DatabaseService, {  } ],

    [ CustomerService, {} ],
    [ AuthorService, {} ],
    [ BookService, {} ],
    [ BookItemService, {} ],
    [ BookLoanService, {} ],

    [ CommandService, { 'commands': {
        'help': CommandHelp(),
        'stop': CommandStop(),

        'customer/list': CommandCustomerList(),
        'customer/create': CommandCustomerCreate(),
        'customer/edit': CommandCustomerEdit(),
        'customer/delete': CommandCustomerDelete(),

        'author/list': CommandAuthorList(),
        'author/create': CommandAuthorCreate(),
        'author/edit': CommandAuthorEdit(),
        'author/delete': CommandAuthorDelete(),

        'book/list': CommandBookList(),
        'book/search': CommandBookSearch(),
        'book/create': CommandBookCreate(),
        'book/edit': CommandBookEdit(),
        'book/delete': CommandBookDelete(),

        'book-item/list': CommandBookItemList(),
        'book-item/create': CommandBookItemCreate(),
        'book-item/delete': CommandBookItemDelete(),

        'book-loan/list': CommandBookLoanList(),
        'book-loan/create': CommandBookLoanCreate(),
        'book-loan/delete': CommandBookLoanDelete()
    } } ]
]
