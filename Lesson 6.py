# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):  # Если работаем со списком, то передаём его длину #Он выводит с индексами
#     # print(i, end=" ")
#     print(a[i] + 2, end=" ")
# # 2 подход
# for i in a:
#     print(i + 2, end=" ")  # этот не может определять индексы, он выводит все сразу
# # Индекс - номер значения


# Задача, которую решаем по обращению к элементу
# a = [int(input("->")) for i in range(int(input("Введите числа для списка:")))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")

# 2 способ
# a = [int(input("->")) for i in range(int(input("Введите числа для списка:")))]
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")


# Вывод числа, который больше предыдущего элемента
# a = [int(input("->")) for i in range(int(input("Введите числа для списка:")))]
#
# for i in range(1, len(a)):
#     if a[i] > a[i > 1]:
#         print(a[i], end="")

# 2 способ НЕ ПРАВИЛЬНЫЙ БЕЗ ИНДЕКСА
# a = [int(input("->")) for i in range(int(input("Введите числа для списка:")))]
# for i in a:
#     if i > i - 1:
#         print(i, end="")

# ЗАДАЧА
# a = range(21, 41)
# sum = 0
# kol = 0
# for i in range(len(a)):
#     if a[i] % 2 == 1:
#         sum += a[i]
# print("Сумма нечётных:", sum)
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         kol += 1
#     else:
#         sum += a[i]
# print("Четные:", kol)

# Задача ср арефм
# a = [int(input("->")) for i in range(int(input("Введите числа для списка:")))]
# sum = 0
# kol = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         sum += a[i]
#         kol += 1
# print(sum / kol)

# меняем элемент по индексу
# lst = [7, 9, 2, 1, 17]
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# Срез
# список[start, stop, step]
# s = [9, 7, 2, 1, 17]
# print(s[1: 4])  # От 1 индекса до 4 не включая 4
# print(s[2:])  # после
# print(s[:2])  # до
# print(s[::2])  # каждый 2 элемент
# print(s[::-1])  # развернули
# print(s[0:-1])  # не выводит последний элемент
# print(s[-1:0:-1])  # почти разворачивает все элементы

# Задача на срезы
# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[::-7])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# СТрока
# st = "Hello World"
# print(st[1:3])
# print(st[::-1])

# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))

# Добавление нескольких элементов
# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# print(lst)
# lst[10:1] = [100]
# print(lst)


#  Методы списка
# lst = list(range(1, 8))
# print(lst)
# lst.append(89)  # Добавляет элемент в конец списка
# print(lst)
# lst.extend([1, 2, 3])  # Добавляет несколько элементов в конец
# print(lst)
# # lst.extend(["add"])  # Можно и строчный
# # print(lst)
# lst.insert(0, 100)  # добавляем элемент по опредедлённому индексу
# print(lst)


# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# 2 спосб
# for element in a:
#     if element in b and element not in c:  # [2, 1, 4, 3, 4, 2]
# c.append(element)print(c)
