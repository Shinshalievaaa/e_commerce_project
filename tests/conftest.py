import pytest

from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

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
        products_str += f'{product}\n'
    return products_str


@pytest.fixture
def product_value():
    return [Product('Rice', 'brown rice', 650, 150)]


@pytest.fixture
def product_smartphone1():
    return Smartphone('Samsung', 'Samsung A33', 100000, 30,
                    'Max. frequency, 2750 MHz; CPU cores, 8 ', 'A33', 8, 'black')


@pytest.fixture
def product_smartphone2():
    return Smartphone('Samsung', 'Samsung S33', 180000, 20,
                    'Max. frequency, 2750 MHz; CPU cores, 8 ', 'S33', 8, 'white')


@pytest.fixture
def product_lawn_grass1():
    return LawnGrass('LawnGrass from Chine', 'the lawn grass is thick', 5000, 100,
        'Chine', '1 month', 'green')


@pytest.fixture
def product_lawn_grass2():
    return LawnGrass('LawnGrass from USA', 'the lawn grass is thick', 3000, 200,
        'USA', '2 month', 'green')
