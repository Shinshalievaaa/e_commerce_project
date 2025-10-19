class Product:
    """Класс товар для электронного магазина"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """строковое отображение"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """сложить полную стоимость двух товаров"""
        return self.quantity * self.__price + other.quantity * other.__price

    @classmethod
    def new_product(cls, data, products_list=None):
        if products_list is None:
            return cls(
                data["name"], data["description"], data["price"], data["quantity"]
            )
        else:
            for product in products_list:
                if product.name == data["name"]:
                    product.price = max(product.price, data["price"])
                    product.quantity = product.quantity + data["quantity"]
                    return product
            return cls(
                data["name"], data["description"], data["price"], data["quantity"]
            )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
