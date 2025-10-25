class PrintMixin:
    """ класс-миксин, который при создании объекта, печатает информацию о том,
    от какого класса и с какими параметрами был создан объект. """
    def __init__(self, name, description, price, quantity):
        print(repr(self))

    def __repr__(self) -> str:
        return f"Product('{self.name}','{self.description}', {self.price}, {self.quantity})"