from src.product import Product


class LawnGrass(Product):
    """Подкласс Смартфон"""
    __price: float

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) == LawnGrass:
            return self.quantity * self.__price + other.quantity * other.__price
        else:
            raise TypeError()