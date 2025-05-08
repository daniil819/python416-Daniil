# Функторы
# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         print("")
#         self.func(a, b)
#         print("После вызова")
#         return f"Перед функцией \n{self.func(a, b)} \nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     print("text")
#     return a * b
#
#
# print(func(2, 5))

# Задача
# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 3))

# задание
# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         print("")
#         self.func(*args, **kwargs)
#         print("После вызова")
#         return f"Перед функцией \n{self.func(*args, **kwargs)} \nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     print("text")
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func2(2, 5, 4))

# задание как можно записать декоратор
# class MyDecorator:
#     def __init__(self, agr):
#         self.name = agr
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             print(self.name)
#             return f"Перед функцией \n{fn(*args, **kwargs)} \nПосле вызова функции"
#
#         return wrap
#
#
# @MyDecorator("test")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# Декоратор с аргументом
# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             return func(a, b) ** self.arg
#
#         return wrapper
#
#
# @Power(3)
# def multiply(a, b):
#     return a * b
#
#
# @Power(5)
# def multiply1(a, b):
#     return a + b
#
#
# print(multiply(2, 2))
# print(multiply1(3, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# # Способ записи
# # class MyList(list):
# #     def get_length(self):
# #         return len(self)
# MyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_length())

# Создание модулей
# import geometry.rect
# import geometry.sq
# import geometry.trian
from geometry import rect, sq, trian
# from geometry import *
def ran()
r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)

s1 = sq.Square(10)
s2 = sq.Square(20)

t1 = trian.Triangle(1, 2, 3)
t2 = trian.Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]

for g in shape:
    print(g.perimeter())

if __name__ == "Lesson32oop":
    ran()