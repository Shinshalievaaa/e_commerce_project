import pytest


def test_add_lawn_grass(product_lawn_grass1, product_lawn_grass2):
    num = product_lawn_grass1 + product_lawn_grass2
    assert num == 1100000


def test_add_lawn_grass_error(product_lawn_grass1):
    with pytest.raises(TypeError):
        product_lawn_grass1 + 1000


def test_add_lawn_grass_error2(product_lawn_grass1, product_smartphone1):
    with pytest.raises(TypeError):
        product_lawn_grass1 + product_smartphone1
