class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def get_category(self):
        if self.price >= 5000:
            return "Expensive"
        return "Affordable"

    def __str__(self):
        return (
            f"Product ID: {self.product_id}, "
            f"Product Name: {self.product_name}, "
            f"Price: ₹{self.price}, "
            f"Category: {self.get_category()}"
        )


class Inventory:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print(f"\nProducts in {self.name}:\n")
        if not self.products:
            print("No products available.")
            return
        for product in self.products:
            print(product)


def main():
    inventory = Inventory("Retail Inventory")

    inventory.add_product(Product("P001", "Laptop", 65000))
    inventory.add_product(Product("P002", "Headphones", 1800))
    inventory.add_product(Product("P003", "Smartwatch", 7800))
    inventory.add_product(Product("P004", "Keyboard", 2300))

    inventory.display_products()


if __name__ == "__main__":
    main()
