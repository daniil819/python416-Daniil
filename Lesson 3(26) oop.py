# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotinuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     for j in range(self.__width):
#         #         print("*", end="")
#         #     print()
#         # 2 способ в одну строку
#         print(("*" * self.__width + "\n")* self.__length)
#
# r1 = Rectangle(4, 2)
# r1.set_width(9)
# r1.set_length(3)
# print("Длина прямоугольника:", r1.get_length())
# print("Ширина прямоугольника:", r1.get_width())
# print("Площадь:", r1.get_area())
# print("Периметр:", r1.get_perimetr())
# print("Гипотенуза", r1.get_hypotinuse())
# r1.get_draw()


# __slots__
# class Point:
#     __slots__ = "x", "y", "z"  # Если больше 1 элемента то можно не ставить скобки
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.x, p1.y, p1.z)
# # print(p1.__dict__)

# property
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         # print("Вызов __get_coord_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         # print("Вызов __set_coord_x")
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Неверный формат")
#
#     @x.deleter
#     def x(self):
#         print("удаление свойства")
#         del self.__x
#
#     # x = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# # print(p1.__set_coord_x(50))
# p1.x = 60  # set
# print(p1.x)  # get
# del p1.x  # del
# print(p1.__dict__)

# Задача на декораторы
# class Persone:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.__old = year
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Persone("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.__dict__)
# p1.old = "31"
# print(p1.__dict__)
# del p1.old
# print(p1.__dict__)

#  Декоратор @staticmethod
# class Point:
#     __count = 0  # Снаружи не будет видно
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod  # Не привязываеться к чему либо и монжно вывести через имя класса
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
# print(Point.get_count())
# print(p1.get_count())


# Static
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10), ch.dec(10))

# Задача
class Numbers:
    @staticmethod
    def max(a, b, c, d):
        mx = a
        if b > mx:
            mx = b
        if c > mx:
            mx = c
        if d > mx:
            mx = d
        return mx

    @staticmethod
    def min(*args):
        mn = args[0]
        for i in args:
            if i < mn:
                mn = i
        return mn

    # @staticmethod
    # def average(*args):
    #     return sum(args) / len(args)
    # 2 способ
    @staticmethod
    def average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


print("Mакс Число", Numbers.max(3, 5, 7, 9))
print("Мин Число", Numbers.min(3, 5, 7, 9))
print('Cр', Numbers.max(3, 5, 7, 9))
print("Факториал", Numbers.factorial(5))
