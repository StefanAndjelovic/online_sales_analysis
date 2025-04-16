from products import Product
from product_manager import ProductManager

def main():
    # Kreiranje instance ProductManager
    manager = ProductManager()

    # Dodavanje nekoliko proizvoda
    manager.add_product(Product("Laptop", 120000, 5))
    manager.add_product(Product("Telefon", 60000, 10))
    manager.add_product(Product("Televizor", 80000, 3))
    manager.add_product(Product("Miš", 2000, 20))

    # Prikaz svih proizvoda
    print("Dostupni proizvodi:\n")
    print(manager.display_all_products())
    print()

    # Prikaz ukupne vrednosti inventara
    print(manager.total_value())
    
    # Testiranje funkcionalnosti uklanjanja proizvoda
    print(manager.remove_product("Telefon"))
    print(manager.display_all_products())
    print(manager.remove_product("Televizor"))
    print(manager.display_all_products())
    
    # Prikazuje ukupne vrednosti inventara
    print(manager.total_value)

if __name__ == "__main__":
    main()