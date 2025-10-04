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