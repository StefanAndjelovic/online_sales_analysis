import random
from products import Product
from product_manager import ProductManager
from cart import Cart

def main():
    # Kreiranje instance ProductManager
    manager = ProductManager()

    # Dodavanje proizvoda
    manager.add_product(Product("Laptop", 120000, 5))
    manager.add_product(Product("Telefon", 60000, 10))
    manager.add_product(Product("Televizor", 80000, 3))
    manager.add_product(Product("Miš", 2000, 20))
    manager.add_product(Product("Tastatura", 3500, 15))

    # Prikaz svih proizvoda
    print("Dostupni proizvodi:\n")
    print(manager.display_all_products())
    print()

    # Kreiranje instance Cart
    cart = Cart()

    # Odabir tri slučajna proizvoda iz liste dostupnih proizvoda
    available_products = manager.products
    random_selection = random.sample(available_products, min(3, len(available_products)))

    for product in random_selection:
        quantity = random.randint(1, product.quantity)  # Random količina unutar dostupnog stanja
        print(cart.add_to_cart(product, quantity))

    # Prikaz korpe i ukupne vrednosti
    print("\nSadržaj korpe:")
    print(cart.display_cart())
    print(cart.calculate_total())

if __name__ == "__main__":
    main()