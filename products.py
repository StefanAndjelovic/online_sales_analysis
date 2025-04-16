class Product:
    def __init__(self, name, price, quantity):
        """Inicijalizacija proizvoda sa imenom, cenom i količinom."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Metod za prikaz informacija o proizvodu."""
        return f"Proizvod: {self.name}, Cena: {self.price} RSD, Količina: {self.quantity}"

    def update_quantity(self, amount):
        """Metod za ažuriranje količine proizvoda."""
        if amount < 0 and abs(amount) > self.quantity:
            return "Greška: Nedovoljna količina na stanju!"
        self.quantity += amount
        return f"Ažurirana količina {self.name}: {self.quantity}"

# Primer korišćenja
product1 = Product("Laptop", 120000, 5)
print(product1.display_info())
print(product1.update_quantity(-2))
print(product1.display_info())