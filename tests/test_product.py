import pytest

from src.product import Product


@pytest.fixture
def product_pasta():
    return Product('Italian pasta', 'durum wheat pasta', 230, 1230)


def test_init(product_pasta):
    """тестирование создания класса продукт"""
    assert product_pasta.name == 'Italian pasta'
    assert product_pasta.description == 'durum wheat pasta'
    assert product_pasta.price == 230
    assert product_pasta.quantity == 1230


def test_new_product(product_json, product_list):
    """тестирование создания нового продукта через метод класса"""
    new_product = Product.new_product(product_list, **product_json)
    assert new_product.name == product_json['name']
    assert new_product.description == product_json['description']
    assert new_product.price == product_json['price']
    assert new_product.quantity == product_json['quantity']


def test_new_double_product(product_json, product_phones_list):
    """тестирование создания существующего продукта"""
    new_product = Product.new_product(product_phones_list, **product_json)
    assert new_product.name == product_json['name']
    assert new_product.description == product_json['description']
    assert new_product.price == product_json['price']
    assert new_product.quantity == 8


def test_price(product_pasta):
    """тестирование изменения цены продукта"""
    product_pasta.price = -10
    assert product_pasta.price == 230
    product_pasta.price = 250
    assert product_pasta.price == 250
