import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_type(product_list):
    return Category('grocery',
                    'dry food products with a long shelf life - cereals and pasta, flour, sugar, etc.',
                    product_list)


def test_init(category_type, products_str):
    """тестирование создания класса категория и проверка добавления нового товара в список и
    проверка на тип добавляемого объекта"""
    assert category_type.name == 'grocery'
    assert category_type.description == 'dry food products with a long shelf life - cereals and pasta, flour, sugar, etc.'
    assert category_type.products == products_str
    assert category_type.number_of_categories == 1
    assert category_type.product_count == 4
    category_type.add_product(Product('Rice', 'brown rice', 650, 150))
    assert category_type.product_count == 5
    assert str(category_type) == 'grocery, количество продуктов: 3730 шт.'


def test_add_product(category_type, product_value, product_smartphone_1, product_lawn_grass_1):
    """ тестирование добавления продуктов в список категории"""
    category_type.add_product(product_value)
    category_type.add_product(product_smartphone_1)
    category_type.add_product(product_lawn_grass_1)
    assert category_type.product_count == 12


def test_add_product_error(category_type):
    """ тестирование добавления не класса Продукт """
    with pytest.raises(ValueError):
        category_type.add_product('onion3')


def test_add_product_error2(category_type):
    """ тестирование добавления не класса Продукт """
    with pytest.raises(ValueError):
        category_type.add_product(Category('test ','test category',[]))