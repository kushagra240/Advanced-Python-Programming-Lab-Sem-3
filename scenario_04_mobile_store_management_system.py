class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_category(self):
        if self.price >= 40000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        return "Budget"

    def __str__(self):
        return (
            f"Brand: {self.brand}, "
            f"Model: {self.model}, "
            f"Price: ₹{self.price}, "
            f"Category: {self.get_category()}"
        )


class Store:
    def __init__(self, name):
        self.name = name
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        print(f"\nMobiles in {self.name}:\n")
        if not self.mobiles:
            print("No mobiles available.")
            return
        for mobile in self.mobiles:
            print(mobile)


def main():
    store = Store("SmartCell Store")

    store.add_mobile(Mobile("Apple", "iPhone 15", 79999))
    store.add_mobile(Mobile("Samsung", "Galaxy A54", 32000))
    store.add_mobile(Mobile("Realme", "Narzo 60", 18000))
    store.add_mobile(Mobile("OnePlus", "OnePlus 11", 66999))

    store.display_mobiles()


if __name__ == "__main__":
    main()
