from order import Order

class Customer:
    def __init__(self, name):
        self.name = name  # invokes setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1–15 characters.")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        if not spending:
            return None
        return max(spending, key=spending.get)
