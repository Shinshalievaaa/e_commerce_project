from src.product import Product


class Category:
    """Класс категория для электронного магазина"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.__products.append(product)
            Category.product_count += 1
        Category.category_count += 1

    def __str__(self):
        """строковое отображение"""
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product):
        if isinstance(product, Product) and issubclass(product.__class__, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product}\n"
        return products_str

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products])/len(self.__products)
        except ZeroDivisionError:
            return 0
