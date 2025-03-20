# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({v: k for k, v in d.items()})  # Поменяли ключи местами со значениями

# Задача 1 на вывод определённых значений
# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({k: v for k, v in d.items() if v <= 2})

# Умножение значений словарей
# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
# s = "Hello"
# d1 = {i: i * 3 for i in s}
# print(d1)

# Задача 2 строковый - ключами, а числовые - значениями
# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in lst:
#     if type(i) is str:  # type(i) == str
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# Функция Zip
# zip([], [])
# обьеденяет несколько последовательностей в одну

# d = dict(zip([1, 2, 3, 4], ['one', 'two', 'three']))
# print(d)
#
# d1 = list(zip([1, 2, 3, 4], ['one', 'two', 'three'], [True, False]))
# print(d1)


# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

#
# a = [1, 2, 3]
# c = list(zip(a))
# print(c)

# Как zip может нам помочь

# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)  # * - работает как распаковка кортежа
# print(a)
# print(b)

# Сортировка значений
# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)

# 1 вариант
# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(number, letter))
# print(data2)
# data2.sort()
# print(data2)
# d3 = dict(data2)
# d3 = {v: k for k, v in data2}

# 2 вариант
# data = sorted((d.items()))
# print(data)


# Распаковка
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# Сложение **
# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})

# Нумерация
# colors = ["red", "yellow", "green"]
# i = 1
# # for color in colors:
# #     print(i, ")", color, sep="")
# #     i += 1
# print()
# for j, color in enumerate(colors, 1):  # enumerate автоматически нумерует
#     print(j, ") ", color, sep="")


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")

# Функции
# def func(*args):  # * - параметр
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))
# print(summa(7, 8, 9))


# Задача на среднее арифметическое
# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#
#     return []
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))


# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(5, 6))
# print(func(1, 2, 3, 4, 5))

# Вывод данных по студентам
# def scores(student, *score):
#     print("Student Name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 5, 5, 4, 3, 3, 5)
# scores("Ivan", 4, 3, 3)


# 2 вариант
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(st="python"))


def info(**data):
    for k, v in data.items():
        print(k, ":", v)
    print()


info(name="Irina", surname="Vetrova", age=22)
info(name="Igor", phone="456789", age=22, email="igor@mail.ru")
