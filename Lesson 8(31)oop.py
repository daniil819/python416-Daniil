# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             return IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым - положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[20] = 4
# # print(s1.marks)
# del s1[2]
# print(s1.marks)
from random import choice


# Задача со временем
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть числом")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return (self.sec // 60) % 60
#         if item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError("Индекс должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# c1['hour'] = 10
# c1["min"] = 20
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])

# Задача
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 9))]
#         else:
#             raise TypeError("Type are not supported")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elza", 5, "F")
# # cat3 = Cat("Murzik", 5, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)

# Полиморфизом

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.perimetr())

# Задача на полиморфизм
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()

# Задача
# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age} ", end=" ")
#
#
# class Student(Human):
#     def __init__(self, name, surname, age, speciality, groups, rating):
#         super().__init__(name, surname, age)
#         self.speciality = speciality
#         self.groups = groups
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.groups} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, name, surname, age, dicipline, exp):
#         super().__init__(name, surname, age, )
#         self.dicipline = dicipline
#         self.exp = exp
#
#     def info(self):
#         super().info()
#         print(f"{self.dicipline} {self.exp}", end="")
#
#
# class Graduate(Student):
#     def __init__(self, name, surname, age, speciality, groups, rating, theme):
#         super().__init__(name, surname, age, speciality, groups, rating, )
#         self.theme = theme
#
#     def info(self):
#         super().info()
#         print(f"{self.theme}")
#
#
# group = [
#     Student("Даши", "Батодалаев", 16, "ГК", "Web_011", 5),
#     Student("Линар", "Загидуллин", 32, "РПО", "PD_011", 5),
#     Teacher("Андрей", "Даньшин", 38, "Астрофизика", 110),
#     Graduate("Сергей", "Шугин", 15, "РПО", "PD_011",
#              5, "Защита персональных данных")
# ]
# for i in group:
#     i.info()

# Функторы
# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(self.count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


def string_strip(chars):
    def wrap(string):
        if not isinstance(string, str):
            raise ValueError("Аргумент должен быть строкой")
        return string.strip(chars)

    return wrap


s1 = string_strip("?:!.;")
print(s1("  Hello world! ..."))


class StringStrip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Должен быть строкой")
        return args[0].strip(self.chars)


s2 = StringStrip("?:!.;")
print(s2("  Hello world! ..."))
