class Auto:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage


class Electro(Auto):
    def __init__(self, power):
        self.power = power

    def info(self):
        print(f"Этот автомобиль имеет мощность {self.power}%")
