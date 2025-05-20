from customer import Customer
from coffee import Coffee


bob = Customer("Bob")
alice = Customer("Alice")

latte = Coffee("Latte")
mocha = Coffee("Mocha")


bob.create_order(latte, 3.75)
bob.create_order(mocha, 4.50)
alice.create_order(latte, 3.25)


print("Customers:")
for c in {bob, alice}:
    print(f"- {c.name}")


print("\nOrders by customer:")
for customer in [bob, alice]:
    print(f"{customer.name} ordered:")
    for order in customer.orders():
        print(f"  - {order.coffee.name}: ${order.price}")


print("\nAverage price per coffee:")
for coffee in [latte, mocha]:
    print(f"{coffee.name}: ${coffee.average_price()}")
