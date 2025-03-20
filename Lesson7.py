# Метод count
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# num = a.count(6)
# print(num)

# Старый способ дз
# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i = 0
# for element in lst:
#     k = element
#     for j in lst:
#         if k == j:
#             i += 1
#     if i == 1:
#         new_lst.append(k)
#     i = 0
# print(new_lst)


# Прошлое дз
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in a:  # 1, 3, 5, 6, 2, 4, 6, 1, 2, 7
#     # print(i, end=" ")
#     if a.count(i) == 1:  # 1 == 1
#         print(i, end=" ")  # 3 5 4 7
# print()
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8 9
#     # print(a[i], end=" ")
#     if a.count(a[i]) == 1:
#         print(a[i], end=" ")


# Задача забор значений из \списка комбинация
# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# for i in range(len(a)):  # Приходят значения 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3,5)
#     c.append(b[i])
# print(c)

# 2 cпособ
# a = [1, 2, 3, 55, 66]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     print(c)

# Удаление
# lst = [11, 1, 22, 2, 33, 3, 55, 66]
#
# lst[5:] = []  # Удаляет элементы от 5 индекса
# # lst[:] = []  # Очистка всего списка
# del lst[:]  # Сокращение от delete
# print(lst)

# lst.remove(22)  # Удаляет элемент из списка по значению(первое вхождение)
# print(lst)
#
# last = lst.pop()  # удаляет последний элемент из списка и возвращамет его
# print(last)
# print(lst)
#
# second = lst.pop(-2)  # удаляет элемент по индексу и может вернуть его
# print(second)
# print(lst)
#
# lst.clear()  # Удаляет все элементы из списка
# print(lst)


# Задача пользователь делает список и удаляет определённый элемент
# print("Введите элемент списка")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс")
# k = int(input("k ="))
# a.pop(k)
# print(a)


# МЕТОД INDEX
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# value = 100
# if value in lst:  # Проверяем находиться ли value в списке
#     ind = lst.index(value, 5, 8)  # возвращает индекс первого вхождения искомого элемента,
#   # можно указать от какого до какого индекса ищем, может выбрасываться исключение ValueError - если элемент не найден
#     print(ind)
# print(lst)

# Copy и id
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# a = lst.copy()
# print(lst, id(lst))
# print(a, id(a))
#
# a.append(100)
# print(lst)
# print(a)
#
# lst[0] = 256
# print(lst)
# print(a)


#  reverse
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# lst.reverse()  # развернул список
# print(lst)

# sort - сортировка
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# new_lst = sorted(lst, reverse=True)
# print(lst)
#
# st = 'Hello'
# new_lst = sorted(lst, reverse=True)
# print(new_lst)
# print(st)

# s = ['Витя', 'Серёга', 'Саня', 'Аня']
# s.sort(key=len, reverse=True)  # Сортировка по длине слова без len по алфавиту
# print(s)

# Генерация случайных данных

import random

# print(random.random())
# print(random.randint(5, 10))  # randint = работает как диапазон от какого до какого
# print(random.randrange(5, 10, 2))  # start: stop: step
# print(random.uniform(10.5, 20.5))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# print(random.choices(s, k=3))

# random.shuffle(city_list)  # Перемешать
# random.shuffle(s)
# print(city_list)
# print(s)

# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
