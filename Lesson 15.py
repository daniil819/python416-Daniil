# Анонимные функции (Lambda - выражения)
# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))  # Функция в одну строку
#
# # Lambda с именем
# # 1 вариант
# func = lambda x, y: x + y
# print(func(1, 2))
# # 2 вариант
# func = (lambda x, y: x + y)(1, 2)
# print(func)


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=1: a + b + c)(10, 20))
# print((lambda a=1, b=2, c=3: a + b + c)())
# print((lambda *args: sum(args))(1, 2, 3, 4))


# кортеж
# tpl = (lambda x: x * 2,
#        lambda x: x * 3,
#        lambda x: x * 4,
#        )
# for t in tpl:
#     print(t('abc___'))

# Замыкание с lambda
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))


# Замыкание сс lambda
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(42)
# print(f(3))

# 2 вариант
# outer = lambda n: lambda x: n + x  # Наружная и вложенная функция
# f = outer(42)
# print(f(3))

# 3 Вариант в одну строку
# print((lambda n: lambda x: n + x)(42)(3))

# Задача 1
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6)

# передача готовых функций
# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])  # сортируем по индексу
# lst.sort(key=func)  # передали функцию
# print(lst)
# print(dict(lst))

# Задача на сортировку футболистов
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)

#  lambda по индексу
# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[0](12, 6))
# print(lst[1](12, 6))
# print(lst[2](12, 6))

# Вызов лябмды по ключу
# d = {1: lambda: print("Понедельник"),
#      2: lambda: print("Вторник"),
#      3: lambda: print("Среда"),
#      4: lambda: print("Четверг"),
#      5: lambda: print("Пятница"),
#      6: lambda: print("Суббота"),
#      7: lambda: print("Воскресенье")
#      }
# d[2]()

# lambda условие (if)
# print((lambda a, b: a if a > b else b)(5, 3))


# from random import randint
# s = (lambda lst: [randint(10, 20) for i in range(10)])([])
# print(s)# print([randint(10, 20) for i in range(10)])
# print([i * 2 for i in [1, 2, 3, 4, 5, 6]])


# map(function, iterables), filter(function, iterables )
# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# Кортеж
# t = (2.88, -1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round, t)))

# Словарь
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))

# Задача найти поэлементо сумму списков
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda a, b: a + b, l1, l2)))


# lst = [input("->") for i in range(5)]
# print(lst)
# lst = list(map(int, lst))
# print(lst)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))
# print(tuple(filter(lambda s: s * 3, t)))


# Фильтр
# lst = [66, 90, 68, 59, 76, 69, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))


# from random import randintlst = [randint(1, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))


# Задача
# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))

# Совмещение map и filter
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
print([x ** 2 for x in range(10) if x % 2])
