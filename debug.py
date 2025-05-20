# debug.py

from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
evian = Customer("Evian")
emmanuel = Customer("Emmanuel")

# Create coffees
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create orders
Order(emmanuel, latte, 3.75)
Order(emmanuel, mocha, 4.50)
Order(evian, latte, 3.25)

# Display all customers
print("Customers:")
for customer in [evian, emmanuel]:
    print(f"- {customer.name}")

# Display each customer's orders
print("\nOrders by customer:")
for customer in [evian, emmanuel]:
    print(f"{customer.name} ordered:")
    for order in customer.orders():
        print(f"  - {order.coffee.name}: ${order.price}")

# Display average price per coffee
print("\nAverage price per coffee:")
for coffee in [latte, mocha]:
    print(f"{coffee.name}: ${coffee.average_price()}")
