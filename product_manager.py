from products import Product

class ProductManager:
    def __init__(self):
        """Inicijalizacija menadžera proizvoda sa praznom listom dostupnih proizvoda."""
        self.products = []

    def add_product(self, product):
        """Dodaje proizvod u listu dostupnih proizvoda."""
        self.products.append(product)
        return f"Proizvod '{product.name}' uspešno dodat."

    def display_all_products(self):
        """Prikazuje sve dostupne proizvode."""
        if not self.products:
            return "Nema dostupnih proizvoda."
        return "\n".join([product.display_info() for product in self.products])

    def total_value(self):
        """Izračunava ukupnu vrednost svih proizvoda."""
        total = sum(product.price * product.quantity for product in self.products)
        return f"Ukupna vrednost svih proizvoda: {total} RSD"
    
    def remove_product(self, product_name):
        """Uklanja proizvod prema njegovom imenu."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"Proizvod '{product_name}' uspešno uklonjen."
        return f"Proizvod '{product_name}' nije pronađen."
# Primer korišćenja
if __name__ == "__main__":
    manager = ProductManager()

    product1 = Product("Laptop", 120000, 5)
    product2 = Product("Telefon", 60000, 10)

    print(manager.add_product(product1))
    print(manager.add_product(product2))
    print(manager.display_all_products())
    print(manager.total_value())