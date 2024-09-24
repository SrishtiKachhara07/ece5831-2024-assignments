# main.py
import pricing
net_price1 = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price1)

# 2) import <module_name> as new_name

import pricing as selling_price
net_price2 = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price2)

#  from <module_name> import <name>

from pricing import get_net_price

net_price3 = get_net_price(price=100, tax_rate=0.01)
print(net_price3)


# 4) from <module_name> import <name> as <new_name>: rename the imported objects

from pricing import get_net_price as calculate_net_price

net_price4 = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)
print(net_price4)


# 5) from <module_name> import * : import all objects from a module

from pricing import *
from product import *

tax = get_tax(100)
print(tax)


# Introduction to Python module search path
import sys

for path in sys.path:
    print(path)

# Python __name__ variable example
def calculate_tax(price, tax):
    return price * tax


def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book',  'price': 30},
                {'name': 'Pen', 'price': 5}]

    # print billing header
    print(f'Name\tPrice\tTax')

    # print the billing item
    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")


print(__name__)

if __name__ == '__main__':
    print_billing_doc()

# Python Packages

# main.py
import sales.order
import sales.delivery
import sales.billing


sales.order.create_sales_order()
sales.delivery.create_delivery()
sales.billing.create_billing()

#=================================================

# main.py
from sales.order import create_sales_order
from sales.delivery import create_delivery
from sales.billing import create_billing


create_sales_order()
create_delivery()
create_billing()

#=================================================
# # main.py
from sales import *


order.create_sales_order()
delivery.create_delivery()

# cannot access the billing module

## Python Private Functions
   
# main.py

from mail import *


send('test@example.com','Hello')


#=================================================
# main.py

import mail


mail.send('test@example.com','Hello')




#=================================================
'''i am putting .py files which i had made to complete module package here in comments'''

#=================================================
'''pricing.py
# pricing.py

def get_net_price(price, tax_rate, discount=0):
    return price * (1 + tax_rate) * (1-discount)


def get_tax(price, tax_rate=0):
    return price * tax_rate
'''
#=================================================
'''product.py
# product.py
def get_tax(price):
    return price * 0.1
'''
#=================================================
'''mail.py
# mail.py

__all__ = ['send']

def send(email, message):
    print(f'Sending "{message}" to {email}')

def attach_file(filename):
    print(f'Attach {filename} to the message')
   '''
#=================================================
'''email.py
# email.py

__all__ = ['send']


def send(email, message):
    print(f'Sending "{message}" to {email}')


def attach_file(filename):
    print(f'Attach {filename} to the message')'''
#=================================================
'''billing.py
def calculate_tax(price, tax):
    return price * tax


def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book',  'price': 30},
                {'name': 'Pen', 'price': 5}]

    # print billing header
    print(f'Name\tPrice\tTax')

    # print the billing item
    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")


print(__name__)

if __name__ == '__main__':
    print_billing_doc()'''

#=================================================
'''app.py
'''