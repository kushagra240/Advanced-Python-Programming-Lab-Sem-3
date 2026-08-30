class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def get_category(self):
        if self.price >= 1000000:
            return "Luxury"
        return "Economy"

    def __str__(self):
        return (
            f"Vehicle Number: {self.vehicle_number}, "
            f"Brand: {self.brand}, "
            f"Price: ₹{self.price}, "
            f"Category: {self.get_category()}"
        )


class Showroom:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print(f"\nVehicles in {self.name}:\n")
        if not self.vehicles:
            print("No vehicles available.")
            return
        for vehicle in self.vehicles:
            print(vehicle)


def main():
    showroom = Showroom("Metro Motors")

    showroom.add_vehicle(Vehicle("MH12AB1234", "BMW", 4200000))
    showroom.add_vehicle(Vehicle("MH09CD5678", "Maruti", 650000))
    showroom.add_vehicle(Vehicle("MH14EF9012", "Audi", 2800000))
    showroom.add_vehicle(Vehicle("MH20GH3456", "Hyundai", 920000))

    showroom.display_vehicles()


if __name__ == "__main__":
    main()
