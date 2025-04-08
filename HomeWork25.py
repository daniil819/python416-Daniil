class Car:

    def __init__(self, model, year, author, power, color, price):
        self.model = model
        self.year = year
        self.author = author
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные авто ".center(40, "*"))

        print(f"Модель: {self.model} \nГод выпуска: {self.year} \nПроизводитель: {self.author} "
              f"\nМощность двигателя: {self.power}  \nЦвет: {self.color} \nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self, year):
        if isinstance(year, int):
            return self.year
        else:
            return ValueError("Год должен быть из цифр")

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self, color):
        if isinstance(color, str):
            return self.color
        else:
            return ValueError("Только из строчных символов")

    def set_price(self, price):
        self.price = price

    def get_price(self, price):
        if isinstance(price, int):
            return self.price
        else:
            return ValueError("Только цифры")


h1 = Car("X7 M50i", 2021, "BMW", 543, "White", 10790000)
h1.print_info()

# h1.set_model(input("Введите модель машины:"))
# h1.set_year(input("Год выпуска:"))
# h1.set_author(input("Производитель:"))
# h1.set_power(input("Мощность двигателя в л.c.:"))
# h1.set_color(input("Введите цвет:"))
# h1.set_price(input("Стоимость:"))
# h1.print_info()
