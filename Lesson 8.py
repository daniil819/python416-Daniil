# способ дз
# import random

# a = [random.randint(0, 100) for i in range(10)]
# print(a)
# minimum = a[0]
# for i in range(len(a)):
#     if a[i] < minimum:
#         minimum = a[i]
#         print('Min:', minimum)
#
# if minimum in a:
#     ind = lst.index(minimum)
#     print('Index min:', ind)
#     print('Итог:', a[ind:])

# 3 способ дз
# import random
#
# a = [random.randint(0, 100) for i in range(10)]
# print(a)
# print(len(a))  # Длина списка
# print('Min:', min(a))  # Минимальное число списка
# print('MAX', max(a))  # Максимальное число списка
# print(sum(a))  # Сумма элементов списка

# Задача на нахождение максимального числа и внесение в начало списка
# import random
#
# a = [random.randint(0, 100) for i in range(10)]
# print(a)
# maximus = max(a)
# print(maximus)
# a.remove(maximus)
# a.insert(0, maximus)
# print(a)


# оператор IN
# import random
#
# a = [random.randint(0, 10) for i in range(10)]
# print(2 in a)  # Есть ли 2 в списке
# print(2 not in a)  # 2 не находиться в списке

# Проверка списка на пустоту
# lst = []
# print(bool(lst))  # Булевый тип данных
# if not lst:
#     print('Пустой')
# else:
#     print('Нет')


# Списки, которые могут содержать другие списки(матрицы)
# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, ], [10, 11, 12, 13]]
# # print(a)
# print(len(a))
# print('1 список:', a[0])
# print('2 список:', a[1])
# print('3 список:', a[2])
# print(a[1][2])
# print(a[2][1])

# Вывод чистого списка
# print('Вариант 1')
# for row in range(len(a)):
#     # print(a[row])
#     for col in range(len(a[row])):
#         print(a[row][col], end="\t")
#     print()

# print('Вариант 2')
# for row in a:
#     for x in row:
#         print(x, end="\t")
#     print()


# Модуль math
# import math
#
# print(math.sqrt(4676))  # Корень
# print(math.ceil(3.2))  # округление вверх
# print(math.floor(3.8))  # округление вниз

# Псевдоним модуля
# import math as m
#
# print(m.sqrt(4676))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# берём из модуля всё
# from math import *
#
# print(sqrt(4676))
# print(ceil(3.2))
# print(floor(3.8))

# Указание нужных функций
# from math import sqrt, ceil, floor
#
# print(sqrt(4676))
# print(ceil(3.2))
# print(floor(3.8))

# Какие есть
# import math
# print(dir(math))

# ЧИСЛО PI
# from math import pi
# print(pi)

# ЗАДАЧА введите радиус окружности
# from math import pi
#
# radius = int(input('Введите радиус окружности:'))
# print('Длина окружности:', round(2 * pi * radius, 2))

# IMPORT TIME
# import time
# import locale
#
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.localtime().tm_year)
# res = time.localtime()
# print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/ %d/ %Y, %H:%M:%S`"))
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y, %A"))
#
# n = 1000000.98

# import time
#
# start = time.monotonic()
# pause = 5
# print('Программа запущена')
# time.sleep(pause)
# result = time.monotonic() - start
# print('Программа выполнен за', result, 'секунд')
