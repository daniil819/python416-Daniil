# Параметры по умолчанию
# def func(a, b=0):
#     return a + b
#
#
# print(func(2, 5))
# print(func(b=2, a=5))  # Именованный аргумент
# print(func(2))  # Позиционный аргумент


# Оператор IS
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)

# ОЗУ
# Один адрес
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(90)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# Перезаписывается в новый адрес
# a = "Hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))


# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))


# Кортеж(tuple) неизменяемый тип данных
# lst = [10, 20, 30]
# tpl = (10, 20, 30)  # Кортеж
# print(lst)
# print(tpl)
# # Проверка на размер данных
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# # Обращение к ним по индексу
# print(lst[1])
# print(tpl[1])
# # Меняем значение
# lst[1] = 50
# print(lst)
#
# tpl[1] = 50
# print(tpl)

# Что мы можем сделать с кортежем
# a = 1, 2, 3, 4, 5
# print(a, type(a))

# a = (1, 2, 3)
# print(a, type(a))

# Изменение формата
# a = tuple("Hello")
# print(a, type(a))

# срезы
# a = (1, 2, 3, 4, 5)
# print(a[2])
# print(a[1:2])

# Заполнение элементами
# from random import randint
#
# print(tuple([i + 2 for i in range(10)]))  # добавляем по 2
#
# # print(tuple([int(input("->")) for i in range(5)])) # сами делаем
#
# print(tuple(randint(50, 100) for i in range(10)))  # Рандомно


# Сложение кортежей
# t1 = tuple("Hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(len(t3))
# print(t3.count("l"))
# print(t3.index("l"))  # Индекс первого вхождения
# print(t3.index("l", 0))

# print(t3.count('l'))
# print(t3.count('a'))
# if 'e' in t3:
#     print(t3.index("e"))
# else:
#     print("Такого элемента нет")

# Перебор значений кортежа
# for i in t3:
#     print(i, end="")

# ЗАДАЧА
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  # tpl
#         else:
#             first = tpl.index(el)  # Находим 1 вхождение 8
#             second = tpl.index(el, first + 1) + 1  # Находим 2 вхождение 8 и +1 чтобы включалась 2 8
#             return tpl[first:second]  # tpl[1:5]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 2, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# Какие типы данных можно класть в кортеж
# tpl = (True, 11, "Hi", [4, 5, 6], ["hi", "mir"])
# print(tpl, id(tpl))
# tpl[4][0] = 'new'
# print(tpl, id(tpl))
# tpl[4].append('hello')
# print(tpl, id(tpl))

# Распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # x, y, z = t
#
# x, y, z = 1, 2, 3  # Множественное присваивание
# print(x, y, z)

# Распаковка с помощью функции
# def get_user():
#     name = "Tom"
#     age = 23
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user  # Сохранили все данные в user
# first_name, year, married = get_user()  # Взяли функцию
# print(first_name)
# print(year)
# print(married)

# Преобразование в кортеж
# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))

# Хранение в кортеже. Кортеж в кортеже Вложенный кортеж
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# # print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")

# ЗАДАЧА
tpl = tuple(input('Введите строку:'))
print(tpl)
lst = []
for i in range(len(tpl)):
    if tpl[i] not in lst:
        lst.append(tpl[i])

print(lst)
for i in range(len(lst)):
    print("Кол-во", lst[i], "=", tpl.count(lst[i]))
