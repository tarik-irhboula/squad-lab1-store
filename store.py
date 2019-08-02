from collections import namedtuple

Product = namedtuple('Product', ['name', 'price', 'quantity'])


def create_store(name: str):
    return {
        'name': name,
        'inventory': []
    }


def create_inventory_product(name, price, quantity) -> Product:
    return Product(name, price, quantity)
