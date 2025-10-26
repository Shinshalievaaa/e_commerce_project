import pytest
from mypy.typeops import type_object_type

from src.category import Category
from src.utils import read_json, create_objects_from_json


def test_read_json():
    raw_data = read_json("data/products.json")
    assert type(raw_data) == list


def test_create_objects_from_json():
    raw_data = read_json("data/products.json")
    categories = create_objects_from_json(raw_data)
    assert issubclass(type(categories[0]), Category)
