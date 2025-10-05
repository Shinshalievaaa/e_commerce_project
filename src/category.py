from src.product import Product


class Category():
    """Класс категория для электронного магазина"""
    name: str
    description: str
    __products: list
    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
            # products) if products is not None else []
        for product in products:
            self.__products.append(product)
            Category.number_of_products += 1
        Category.number_of_categories += 1


    def add_product(self, Product):
        self.__products.append(Product)
        Category.number_of_products += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return products_str
