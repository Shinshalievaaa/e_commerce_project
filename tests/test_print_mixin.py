from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_print_mixin_roduct(capsys):
    Product('Italian pasta', 'durum wheat pasta', 230, 1230)
    message = capsys.readouterr()
    assert message.out == "Product('Italian pasta','durum wheat pasta', 230, 1230)\n"


def test_print_mixin_smartphone(capsys):
    Smartphone('Samsung', 'Samsung A33', 100000, 30,
               'Max. frequency, 2750 MHz; CPU cores, 8 ', 'A33', 8, 'black')
    message = capsys.readouterr()
    assert message.out == "Product('Samsung','Samsung A33', 100000, 30)\n"


def test_print_mixin_lawnGrass(capsys):
    LawnGrass('LawnGrass from Chine', 'the lawn grass is thick', 5000, 100,
              'Chine', '1 month', 'green')
    message = capsys.readouterr()
    assert message.out == "Product('LawnGrass from Chine','the lawn grass is thick', 5000, 100)\n"

