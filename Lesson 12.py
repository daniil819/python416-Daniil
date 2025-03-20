# Ключи
# d = {i: i ** 2 for i in range(1, 8)}
# print(d)
# print(3 in d)  # Проверка ключа
# print(25 in d)
# # Удаление и ключа и значения
# del d[8]
# print(d)
# Через if
# key = 4
# if key in d:
#     del d[key]
# print(d)


# key = 5
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом ", key, "нету")
# print(d)


# Задача на перемножение всех чисел
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)


# Задача на сохранение слов в словарь с индексами и удаление определённого элемента
# a = dict()
# a[1] = input("->")
# a[2] = input("->")
# a[3] = input("->")
# a[4] = input("->")
# print(a)

# a = {i: input("->") for i in range(1, 5)}
# print(a)
# dis = int(input("Что исключить:"))
# del a[dis]
# print(a)

# Написать программу, которая выводит инфу о товаре
goods = {'1': ['Core-i3-4330 ', 9, 4500],
         '2': ['Core-i5-12433 ', 3, 8500],
         '3': ['Amd FX-6300 ', 6, 3500],
         '4': ['Pentium G4330 ', 7, 9500],
         '5': ['Core-i2-4550 ', 11, 7100]
         }
for i in goods:
    print(i, ')', goods[i][0], '- ', goods[i][1], ' шт ', goods[i][2], 'руб', sep='')
while True:
    n = input("№: ")
    if n == "0":
        break

    else:
        if n in goods:
            try:
                count = int(input("Кол-во:"))
                goods[n][1] = count
                break
            except ValueError:
                print('Значение некорректное. Введите число ')
        else:
            print('Такого ключа не существует')

for i in goods:
    print(i, ')', goods[i][0], '- ', goods[i][1], ' шт ', goods[i][2], 'руб', sep='')

# Методы словарей
# d = {'A': 1, 'B': 2, 'C': 3}
# print(d)
#
# print(d.keys())  # Показывает список ключей
# print(d.values())  # список значений
# print(d.items())  # Список ключей и значений в виде кортежей
#
# for i, j in d.items():
#     i = 0
#     print(i, ':', j)
# print(d)

# d = {'A': 1, 'B': 2, 'C': 3}
# d2 = d.copy()  # Cоздаёться копия словаря
# d2 = d
# print('D =', d)
# print('D2 =', d2)
# d2['B'] = 5
# print('D =', d)
# print('D2 =', d2)

# d = {'A': 1, 'B': 2, 'C': 3}
# # d.clear()  # Очистка словаря
# # item = d.pop("M", 'Такого ключа не существует в словаре') # Удалили элемент по ключу
# item = d.popitem()  # Удаляется последний элемент и возвращается кортеж тз ключа и значения
# print(d)
# print(item)


# d = {'A': 1, 'B': 2, 'C': 3}
# print(d)
# print(d['B'])
# value = d.get('W', 'Такого ключа не существует')  # Получает значение по заданному ключу
# print(value)

# item = d.setdefault("W", 5)  # ПО заданному ключу добавляет ключ и значение, если его не существовало
# print(d)
# print(item)


# d = {'A': 1, 'B': 2, 'C': 3}
# d2 = {"R": 7, "Q": 9, "B": 5}
# d3 = [("T", 7), ("Y", 9)]
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)
# d.update(d3)
# print(d)


# Задача 1 создать словарь и потом удалить из исходного словаря старые значения
# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# # new_d["name"] = d.pop("name")
# # new_d["salary"] = d.pop("salary")
# new_d["name"], new_d["salary"] = d.pop("name"), d.pop("salary")
# # d.pop("name")
# # d.pop("salary")
# print(d)

# Задача 1.1
# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# d['location'] = d.pop('city')
# print(d)


# d = {"first": {1: "one", 2: "two", 3: "three"}, "second": {4: "four", 5: "five"}}
# print(d)
# 1 вариант
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ":", d[x][y], sep=" ")
# 2 вариант
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")
