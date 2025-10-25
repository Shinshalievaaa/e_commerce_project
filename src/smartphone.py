from src.product import Product
from src.print_mixin import PrintMixin


class Smartphone(Product, PrintMixin):
    """Подкласс Смартфон"""

    __price: float

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) == Smartphone:
            return self.quantity * self.__price + other.quantity * other.__price
        else:
            raise TypeError()
