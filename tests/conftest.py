import pytest

from src.product import Product

@pytest.fixture
def product_list():
    product_pasta = Product('Italian pasta', 'durum wheat pasta', 230, 1230)
    product_buckwheat = Product('Makfa buckwheat', 'buckwheat', 150, 900)
    product_flour = Product('Makfa flour', 'first grade flour', 330, 600)
    product_salt = Product('Iletsk salt', 'salt', 50, 850)
    return [product_pasta, product_buckwheat, product_flour, product_salt]


@pytest.fixture
def product_phones_list():
    product_samsung = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_iphone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return [product_samsung, product_iphone]


@pytest.fixture
def product_json():
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 210000.0,
        "quantity": 3
      }


@pytest.fixture
def products_str(product_list):
    products_str = ""
    for product in product_list:
        products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
    return products_str


@pytest.fixture
def product_value():
    return [Product('Rice', 'brown rice', 650, 150)]
