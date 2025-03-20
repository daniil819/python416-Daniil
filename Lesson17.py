# Перфиксы
# print(b'a1b2c2')

# f строка
# name = 'Дима'
# age = 21
# print('Меня зовут ', name, '. Мне ', age, ' лет.', sep="")
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.', )
# print(f'Меня зовут {name}. Мне {age}  лет.', )

# Числа
# x = 10
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x:}, {y:}")
# print(f"{x} x {y} / 2 = {round(x * y / 7, 2)}")
# print(f"{x} x {y} / 2 = {x * y / 7: .3f}")

# Фигурные скобки для каждой нужно  2 скобки
# num = 74
# print(f"{{{num}}}")

# Строки
# dir_name = 'Folder'
# file_name = 'file.txt'
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# Кавычки
# st = ('Многострочный'
#       'текст')
# print(st)
#
# s = '''Многострочный'
#       текст'''
# print(s)
# s1 = """Многострочный
# текст
# """
# print(s1)

# Документация """"""
# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)  # вызов документации
# print(len.__doc__)
# print(min.__doc__)

# документация пайчарама """""" + enter
# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основание высоты и радиуса.
#     :param r: Положительное число, радиус основания цилиндра
#     :param h: Положительное число, Высот  цилиндра
#     :return:
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# ASCII
# print(ord("a"))
# print(ord("#"))
# print(ord("п"))

# while True:
#     n = input('->')
#     if n != -1:
#         print(ord(n))
#     else:
#         break


# Задача прохождение каждого элемента строки
# st = 'Test string for me'
# arr = [ord(x) for x in st]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Cреднее-арефм:', arr)
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# Обратный символ
# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(11234))

# Задача
# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')

# Пароль
# import random
# from random import randint
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 123
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ''
#     for i in range(rand_len):
#
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль:", random_password())

# МЕТОДЫ СТРОК
# s = ' I am learnig Python. hello, WORLD!'
# # print(s.capitalize())  # Hello, world! i. am learning python
# # print(s.lower())  # hello, world! i am learning python
# # print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON
# # print(s.count('h'))  # Считает сколько раз элемент встречается в строке
# print(s.count('h', 1, -4))  # считает наличие элемента от индекса
# # print(s.lower().count('i'))
#
# # print(s.find('Python'))  # показывает индекс
# # print(s.find('h', 1))  # индекс последнего вхождения
# #
# print(s.index('h', 1, -4))
# print(s.rfind('h'))

# # задача
# # 1 вариант
# st = input('->')
# one = st[:st.find('')]  # st[:4]
# two = st[st.find(" "):]  # st[4:]
# res = two + " " + one
# print(res)
# # # 2 вариант
# st = "один два"
#

# нахождение чего либо
# s = "hello, WORLD! I am learning Python."
# print(s.startswith('hello'))
# print(s.startswith('i am', 14))
# print(s.find('I am'))
# print(s.endswith('Python'))

# isalnum()
# print('abc123'.isalnum())  # состоит ли строка из букв и цифр
# print('abc123!'.isalnum())
# print('123'.isalnum())
# print('abc'.isalnum())

# isalpha()
# print('ABCabc'.isalpha())  # состоит ли строка из букв
# print('ABC%abc'.isalpha())

# isdigit()
# print('123'.isdigit())  # состоит ли строка из цифр
# print('123@'.isdigit())

# islower()
# print('aab'.islower())  # находиться ли буква в нижнем регистре, допускаются другие значения
# print('aAbc'.islower())
# print('123aab'.islower())

# isupper()
# print('ABC'.isupper())  # верхний регистр
# print('ABc'.isupper())
# print('ABC1'.isupper())

# center() пробелы
# print('py'.center(10))
# print('py'.center(10, '-'))
# print('py'.center(1))

# удаление пробелов
# print('   py'.lstrip())  # лево
# print('py   '.rstrip())  # право
# print('   py   '.strip())  # обе


# print('https://www.python.org'.lstrip('/;htps'))
# print('https://www.python.org'.lstrip('/;htps').rstrip('.w'))
# print('https://www.python.org'.strip('/;htps .w'))

# Поиск и замена символ
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("N", "P", 2))


# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
# print('..'.join(['1', '99']))
# print('..'.join('Hello'))
