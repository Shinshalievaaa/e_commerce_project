class Product():
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


    @classmethod
    def new_product(cls, products_list, **data):
        for product in products_list:
            if product.name == data['name']:
                product.price = max(product.price, data['price'])
                product.quantity = product.quantity + data['quantity']
                return product
        return cls(data['name'], data['description'], data['price'], data['quantity'])


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price
