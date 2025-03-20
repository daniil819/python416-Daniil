# Декораторы
# Вызываем первую функциию
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am super_func")
#     print(func())
#
#
# super_func(hello)


# Сохранение функции в переменную
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# Пример работы с декораторам
# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()  # тут вызывается  func_test
#         print("Код после функции")
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")


# test = my_decorator(func_test)
# test()


# используем функцию декораторы
# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print("Код до функции")
#         func()  # тут вызывается  func_test
#         print("Код после функции")
#
#     return func_wrapper
#
#
# @my_decorator  # декаратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

# пример 2
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# Задача 1
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# декоратор с аргументами
# def outer(fn):
#     def inner(args1, args2):
#         print('Данные:', args1, args2)
#         fn(args1, args2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', 'Ветрова')


# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("Kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, 'изучают', study, end='\n\n')
#
#
# print_data('Борис', 'Eлизовета', 'Света', study="JS")  # Перезаписали study
# print_data('Владимир', 'Екатерина', "Виктор")  # study по умолчанию

# сложение и тд
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2,  y, '=', end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(2, 5)

# Задача, гед декроратор применяет число
# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат", return_num(5))

# Как работают строки
# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# unicode
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[-1])
# print(e[1:3])

# Задача
# def chang_char_to_str(s, old, new):
#     s2 = ""
#
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, 'N', 'P')
# print(str1)
# print(str2)

# Префиксы
print(u"Привет")
print("Привет")

print("C:\\file.txt\\")
print(r"C:\\file.txt\\"[:-1])
print(r"C:\file.txt" + "\\")
