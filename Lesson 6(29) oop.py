# Абстрактные методы
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp, ep, color, width):
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочерних классах должен быть определён draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep},{self.color}, {self.color}, {self.width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep},{self.color}, {self.color}, {self.width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# shapes = list()
# shapes.append(Line(Point(0, 0), Point(10, 10), "yellow", 10))
# shapes.append(Line(Point(10, 10), Point(20, 20), "red", 6))
# shapes.append(Rect(Point(50, 50), Point(70, 70), "blue", 4))
# shapes.append(Ellipse(Point(80, 80), Point(100, 100), "green", 3))
#
# for i in shapes:
#     i.draw()
from abc import ABCMeta, abstractclassmethod


# Абстрактный метод
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь на е2у4")
#
#
# q = Queen()
# q.draw()
# q.move()


# Задача
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#
# def calc_area(self):
#     raise NotImplementedError("В дочернем классе должен быть определён метод calc_area")
#
#
# class RectangleTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = RectangleTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = RectangleTable(20)
# print(t.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())

# Задача с валютой
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def print_info(self):
#         self.print_value()
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_info()
#
# print("*" * 50)
# for elem in e:
#     elem.print_info()

# Интерфейсы
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()

# Вложенный классы
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_static_method():
#         print("Статический метод")
#
#     def outer_obj_method(self):
#         print("Метод экземпляра", self.name)
#
#     class MyInner:
#         def __init__(self, inner_inner, obj):
#             self.inner_inner = inner_inner
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод внутреннего класса", MyOuter.age, self.obj.name)
#             print(self.inner_inner)
#             MyOuter.outer_static_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("Внешний")
# print(out.name)
# inner = out.MyInner("Внутрений")
# # inner = MyOuter.MyInner("внутри")
# print(inner.inner_inner)


# class Color:
#     def __init__(self):
#         self.name = "Green"
#
#     def show(self):
#         print("Name:", self.name)
#
#
# class LightColor:
#     def __init__(self):
#         self.name = "LightGreen"
#         self.lg = LightColor()
#         self.dg = self.DarkColor()
#
#     def display(self):
#         print("Name:", self.name)
#
#     class DarkColor:
#         def __init__(self):
#             self.name = "DarkGreen"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# g = outer.lg
# g.display()
# g1 = outer.dg
# g1.display()


# Вложенные
class Computer:
    def __init__(self):
        self.name = "PC001"
        self.os = self.OS()
        self.cpu = self.CPU()

    class OS:
        def system(self):
            return "Windows 10"

    class CPU:
        def make(self):
            return "Intel"

        def model(self):
            return "Core-i9"


comp = Computer()
my_os = comp.os
my_cpu = comp.cpu
print(comp.name)
print(my_os.system())
print(my_cpu.make())
print(my_cpu.model())
