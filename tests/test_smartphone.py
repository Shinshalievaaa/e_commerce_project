import pytest


def test_add_smartphone(product_smartphone1, product_smartphone2):
    num = product_smartphone1 + product_smartphone2
    assert num == 6600000


def test_add_smartphone_error(product_smartphone1):
    with pytest.raises(TypeError):
        product_smartphone1 + 1000


def test_add_smartphone_error2(product_smartphone1, product_lawn_grass1):
    with pytest.raises(TypeError):
        product_smartphone1 + product_lawn_grass1
