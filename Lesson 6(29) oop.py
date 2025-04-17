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
from abc import ABC, abstractmethod


class Currency(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def convert_to_rub(self):
        pass

    @abstractmethod
    def print_value(self):
        print(self.value, end=" ")


class Dollar(Currency):
    rate_to_rub = 74.16
    suffix = "USD"

    def convert_to_rub(self):
        return self.value * Dollar.rate_to_rub

    def print_value(self):
        super().print_value()
        print(Dollar.suffix, end=" ")


class Euro(Currency):
    rate_to_rub = 90.14
    suffix = "EUR"

    def convert_to_rub(self):
        return self.value * Euro.rate_to_rub

    def print_value(self):
        super().print_value()
        print(Euro.suffix, end=" ")


d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
e = [Euro(5), Euro(10), Euro(50), Euro(100)]
for elem in d:
    elem.print_value()
    print(f"= {elem.convert_to_rub():.2f} RUB")
print()
for elem in e:
    elem.print_value()
    print(f"= {elem.convert_to_rub():.2f} RUB")
