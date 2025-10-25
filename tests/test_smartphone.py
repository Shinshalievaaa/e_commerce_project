import pytest


def test_add_smartphone(product_smartphone_1, product_smartphone_2):
    num = product_smartphone_1 + product_smartphone_2
    assert num == 6600000


def test_add_smartphone_error(product_smartphone_1):
    with pytest.raises(TypeError):
        product_smartphone_1 + 1000


def test_add_smartphone_error2(product_smartphone_1, product_lawn_grass_1):
    with pytest.raises(TypeError):
        product_smartphone_1 + product_lawn_grass_1
