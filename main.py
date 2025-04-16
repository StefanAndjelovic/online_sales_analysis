import random
from products import Product
from product_manager import ProductManager
from cart import Cart

def main():
    # Kreiranje instance ProductManager
    manager = ProductManager()

    # Dodavanje proizvoda sa izmenjenim imenima i količinama
    manager.add_product(Product("Gaming Laptop", 150000, 3))
    manager.add_product(Product("Pametni Sat", 45000, 8))
    manager.add_product(Product("Bežične Slušalice", 25000, 12))
    manager.add_product(Product("Mehanička Tastatura", 6000, 10))

    # Kreiranje instance Cart
    cart = Cart()

    # Odabir slučajnih proizvoda za dodavanje u korpu
    available_products = manager.products
    random_selection = random.sample(available_products, min(3, len(available_products)))

    for product in random_selection:
        quantity = random.randint(1, product.quantity)
        print(cart.add_to_cart(product, quantity))

    # Prikaz sadržaja korpe
    print("\nSadržaj korpe:")
    print(cart.display_cart())
    print(cart.calculate_total())

if __name__ == "__main__":
    main()