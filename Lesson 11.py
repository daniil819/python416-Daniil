# Множества (set)
# Данные выводят не в определенном порядке и нельзя работать в индексе
# s = {"red", "green", "blue"}
# print(s)
# print(type(s))
# print(len(s))

# Тип данных DICT
# a = {}
# print(a, type(a))


# Как создать пустой set
# a = set('hello')
# print(a, type(a))


# sp = {i * i for i in range(10)}
# print(sp)

# Набор повторяющихся значений
# lst = [10, 2, 2, 2, 2, 2, 28, 8, 8, 8, 8, 8, 4, 5, 9, 9, ]
# # st = {i for i in lst if i % 2 == 0}
# # print(st)
# st = set(lst)
# # print(st)
# lst2 = list(st)  # Преобразование в список
# print(lst2)

# Проверка на наличие того или иного значения
# s = {"red", "green", "blue"}
# print("green" in s)
# print("black" in s)


# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if "a" in i])  # Вывели всю строку и проверили на наличие "a"
# print({i for i in lst if "a" in i})
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))  # iflse в одну строку
# print(tuple("A" if i[0] == "a" else "B" for i in lst))
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == 'c'))

# Роспись более подробно
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
# print(lst2)


# print(dir(set))

# Методы set
# a = {'red', 'yellow', 'green'}
# print(a)
# a.add('black')  # добавляет элемент
# print(a)
#
# a.remove('yellow')  # удаляет по значению
# print(a)

# a.remove('blue')  # keyError
# print(a)

# el = 'green'
# if el in a:
#     a.remove(el)
#
# print(a)

# a.discard('blue')  # удаляет по значению
# print(a)

# a.pop()  # удаляет первый элемент из множества
# print(a)
#
# a.clear()  # Очистили множество
# print(a)

# Операторы объединения и операции с множествами
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)  # или c = a | b объединение в один
# print(c)
# a |= b
# print(a)

# c = a & b
# print(c)
# a &= b
# print(a)

# c = a - b
# print(c)
# a -= b
# print(a)

# a ^= b
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Кол-во уникальных элементов:", len(s))
# print(min(s))
# print(max(s))


# Задача
# s1 = 'Hello'
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# # a = set(s1) & set(s2)
# # print(a)
# # s1 = set(s1)
# # print(s1)
# # s2 = set(s2)
# # print(s2)
# # a = s1 & s2
# for i in a:
#     print(i, end=" ")
#
# print('s1 =', s1)
# print('s2 =', s2)


# Подмножество
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a <= b
# print(c)

# Frozenset замороженные множества
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello", "world"})
# print(a)


# Словарь (dict)
# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
# print(lst[1])
# lst[1] = "ten"
# print(lst)
#
# d["second"] = "ten"
# print(d)

# d = dict(a="hello")
# print(d)
# print(type(d))
#
# d1 = {"a": 'hello', "b": 'world'}
# print(d1)

# Какие типы данных можно хранить в словарях
# Ключами могут быть только не изменяемые типы данных
# d = {0: "text", "one": 45, (1, 2): "Кортеж", 42: [9, 8], True: 1, False: 0, "a": "Кортеж", 1: "один", "a": 56}
# print(d)


user = [['a', 1], ['b', 2], ['c', 3]]
print(user)
new_dict = dict(user)
print(new_dict  )
