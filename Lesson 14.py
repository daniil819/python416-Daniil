# # как обращаться к разным типам
# def func1(*args):
#     print("args", args)
#     print(args[0])  # Обращение к кортежу
#
#
# def func2(**kwargs):
#     print("kwargs", kwargs)
#     print(kwargs['one'])  # Обращение к словарю через ключ
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)

# Области Видимости (scope)
# name = 'Tom'  # Глобальная переменная
#
#
# def hi():
#     global name  # Сделали "Sam" глобальной переменной
#     name = 'Sam'
#     surname = "jonson"  # Локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Goodbye", name)
#
#
# hi()
# bye()
# print(name)

# область builtins
# import builtins
# name = dir(builtins)
# for t in name:
#     print(t)


# enclosing
# x = 4
# def func():
#     x = 2  # 2
#
#     def inner():
#         print("x = ", x)  # 4
#         print(x + 3)
#
#     inner()  # 3
#
#
# func()  # 1


# Вложенные функций
# def outer(who):
#     def inner():
#         print('Hello', who)
#
#     inner()
#
#
# outer('World')

# Как работает вложенные функций
# def fun1():
#     a = 6  # 2
#
#     def fun2(b):
#         a = 4  # 5
#         print("Сумма:", a + b)  # 6
#
#     print('a:', a)  # 3
#     fun2(3)  # 4
#
#
# fun1()  # 1

# nonlocal
# x = 25
# t = 5
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a  # Делаем переменную не локальной
#         a = 35
#         print('a =', a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t  # 25 + 30 = 55 # 25 + 35 = 60
# print(c)

# nonlocal пример
# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()

# пример
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# 1 ЧАСТЬ ДЗ
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# ЗАМЫКАНИЕ НОВАЯ ТЕМА
def outer(n):
    def inner(x):
        return n + x

    return inner


func1 = outer(5)
print(func1(10))

func2 = outer(6)
print(func2(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         print(a)
#         c.append(4)
#         # a = 5
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# Задача на подсчёт посещений
# def func(city):
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(city, n)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()