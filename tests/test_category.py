import pytest

from src.category import Category


@pytest.fixture
def category_type(product_list):
    return Category('grocery',
                    'dry food products with a long shelf life - cereals and pasta, flour, sugar, etc.',
                    product_list)


def test_init(category_type, product_list):
    """тестирование создания класса категория"""
    assert category_type.name == 'grocery'
    assert category_type.description == 'dry food products with a long shelf life - cereals and pasta, flour, sugar, etc.'
    assert category_type.products == product_list
    assert category_type.number_of_categories == 1
    assert category_type.number_of_products == 4
