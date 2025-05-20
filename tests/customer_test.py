import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    try:
        Customer("A" * 16)
        assert False, "Should raise error for long name"
    except ValueError:
        pass

    try:
        Customer("")
        assert False, "Should raise error for empty name"
    except ValueError:
        pass

def test_customer_orders_and_coffees():
    c = Customer("Anna")
    coffee = Coffee("Latte")
    c.create_order(coffee, 3.5)
    assert len(c.orders()) == 1
    assert coffee in c.coffees()
