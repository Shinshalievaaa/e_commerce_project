import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """чтение данных из фала json"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as json_file:
        data = json.load(json_file)
        return data


def create_objects_from_json(data) -> list:
    """создание объектов категорий и товаров из словаря"""
    categories = []

    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    raw_data = read_json("src/products.json")
    categories = create_objects_from_json(raw_data)
    print(categories[0].name)
    print(categories[0].description)
    print(categories[0].products)
