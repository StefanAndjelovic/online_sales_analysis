from products import Product

class Cart:
    def __init__(self):
        """Inicijalizacija korpe kupca sa praznom listom artikala."""
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        """Dodaje proizvod u korpu sa određenom količinom."""
        if quantity > product.quantity:
            return f"Nema dovoljno proizvoda '{product.name}' na stanju!"
        self.cart_items.append((product, quantity))
        product.quantity -= quantity
        return f"Dodato {quantity} x '{product.name}' u korpu."

    def calculate_total(self):
        """Računa ukupnu vrednost korpe."""
        total = sum(product.price * quantity for product, quantity in self.cart_items)
        return f"Ukupna vrednost korpe: {total} RSD"

    def display_cart(self):
        """Prikazuje sve artikle u korpi."""
        if not self.cart_items:
            return "Korpa je prazna."
        return "\n".join([f"{quantity} x {product.name} - {product.price} RSD" for product, quantity in self.cart_items])

# Primer korišćenja
if __name__ == "__main__":
    product1 = Product("Laptop", 120000, 5)
    product2 = Product("Telefon", 60000, 10)

    cart = Cart()
    print(cart.add_to_cart(product1, 2))
    print(cart.add_to_cart(product2, 5))
    print(cart.display_cart())
    print(cart.calculate_total())