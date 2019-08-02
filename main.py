from store import create_store, create_inventory_product


def start_inventory_creation(store):
    while True:
        print(f'You have {len(store.get("inventory"))} products in your inventory')
        choice = input("""
            1) Add new product
            0) return to store
        """)

        if choice == '0':
            break

        name = input('- name:')
        price = input('- price:')
        quantity = input('- quantity:')

        store.get('inventory').append(
            create_inventory_product(name, price, quantity)
        )


def start_store():
    name = input('Would you like to name it ?')

    store = create_store(name)
    print(f'Welcome to {name}')

    while True:
        choice = input("""
            What do you want to do ?
             1)- Update inventory
             0)- Exit
        """)

        if choice == '0':
            break

        if choice == '1':
            start_inventory_creation(store)

    print(store)


if __name__ == '__main__':
    start_store()
