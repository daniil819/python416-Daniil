# # Магические методы
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):  # Вызываем когда обращаемся к экземпляру класса
#         return f"{self.name}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

## __slots__
# import math
#
#
# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(23, 22)
# # p1.z = 30
# p1.length = 10
# print(p1.length)

# __sizeof__
# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# p2 = Point2D(10, 20)
# print("p1=", p1.__sizeof__())
# print("p2=", p2.__sizeof__() + p2.__dict__.__sizeof__())


#  Наследование
# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = "z"
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# pt3.z = 30
# print(pt3.z)
# # print(pt3.__dict__)

# # Множественное наследование
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleep")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")  # Берёт данные из первого класса
# dog.bark()
# dog.sleep()
# dog.play()

# Супер множественное наследование
# class A:
#     def __init__(self):
#         print("Инициализация класса A")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализация класса AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализация класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализация класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализация класса D")
#
#
# d = D()
# print(D.mro())
# print(D.mro())

# Пример
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализация styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализация Pos")
#         self.sp = sp
#         self.ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100))
# l1.draw()

# Миксин
# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар продан в 17:15")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()

# Перезагрузка операторов
# Число секунд в одном дне: 24 * 60 * 60 = 86400
# # ДЛЯ ДЗ
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
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ValueError("Правый операнд должен быть Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ValueError("Правый операнд должен быть Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(100)
# c2 = Clock(100)
#
# # c4 = Clock(300)
# # c3 = c1 + c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c3.get_format_time())
# # print(c4.get_format_time())
# if c1 != c2:
#     print("Время равно")
# else:
#     print("Время разное")


class Student:
    def __init__(self, name, *marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        return self.marks[item]


s1 = Student("Сергей", 5, 5, 3, 4, 5, 4, 5)
print(s1.marks[2])
print(s1[2])
