
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    c = Customer("Tom")
    coffee = Coffee("Espresso")
    try:
        Order(c, coffee, 0.5)
        assert False, "Price below 1.0 should fail"
    except ValueError:
        pass

    try:
        Order(c, coffee, 11.0)
        assert False, "Price above 10.0 should fail"
    except ValueError:
        pass

def test_order_association():
    c = Customer("Mia")
    coffee = Coffee("Cappuccino")
    order = Order(c, coffee, 5.0)
    assert order.customer == c
    assert order.coffee == coffee
