import pytest

from src.product import Product

@pytest.fixture
def product_list():
    product_pasta = Product('Italian pasta', 'durum wheat pasta', 230, 1230)
    product_buckwheat = Product('Makfa buckwheat', 'buckwheat', 150, 900)
    product_flour = Product('Makfa flour', 'first grade flour', 330, 600)
    product_salt = Product('Iletsk salt', 'salt', 50, 850)
    return [product_pasta, product_buckwheat, product_flour, product_salt]