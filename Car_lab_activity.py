class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = Car("Toyota", "Land Cruiser", 2025)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Ford", "Mustang", 2024)

for car in (car1, car2, car3):
    print(f"{car.brand} {car.model} ({car.year}) - Wheels: {car.wheels}")