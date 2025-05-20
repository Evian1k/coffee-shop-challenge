
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_validation():
    try:
        Coffee("AB")
        assert False, "Should raise error for short name"
    except ValueError:
        pass

def test_average_price():
    coffee = Coffee("Mocha")
    c1 = Customer("Ben")
    c2 = Customer("Eve")
    c1.create_order(coffee, 2.0)
    c2.create_order(coffee, 4.0)
    assert coffee.average_price() == 3.0
