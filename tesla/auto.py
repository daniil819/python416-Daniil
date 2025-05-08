class Auto:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.mileage} км")