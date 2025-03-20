# Функция
# def -define (Определить)

# Как её вызывать
# def hello(name, age):   # hello - имя функции
#     print("Меня зовут " + str(name) + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)


# Как можно ещё записать
# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)

# Задача вывод на экран линий
# def print_line(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")


# return
# def get_sum(a, b):
#     return a + b  # возвращает значение из функции и добавляет в res
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print(get_sum(5, 10))

# проверка
# def func():
#     print('Внутри функции = ', res)
#
#
# func()


# Функции return

# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9, 2))
# print(max_value(1, 123))


# ЗАДАЧА НА РАЗНОСТЬ и СУММЫ
# def add(x, y):
#     if x > y:
#         return x - y
#     elif x < y:
#         return x + y
#
#
# a = int(input('Введите число 1:'))
# b = int(input('Введите число 2:'))
# print(add(a, b))


# Задача на change
# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# задание
# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(is_first_big(10, 5))
# # print(is_first_big(1, 5))
# a = int(input('Введите число 1:'))
# b = int(input('Введите число 2:'))
# if is_first_big(a, b):
#     print("Первое > второго")
# else:
#     print("Второе < первого")


# Проверка пароля
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if 'A' <= ch <= "Z":  # Проверяем весь алфавит и на наличие больших букв
#             has_upper = True
#         if 'a' <= ch <= "z":  # Проверяем пароль на наличие маленьких букв
#             has_lower = True
#         if "0" <= ch <= "9":  # проверяем на наличие символов
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:  # Проверяем на наличие кол-во чисел
#         return True
#     return False
#
#
# p = input("Введите пароль:")
# if check_password(p):
#     print('Надёжный')
# else:
#     print('Надо менять')


# 4 принимаемых аргумента
def get_sum(a, b, c=0, d=1):
    return a + b + c + d


# print(get_sum(7, 9, d=3, c=5))
# print(get_sum(1, 2, 3, 4))
# print(get_sum(1, 6, 7))
# print(get_sum(1, 5, d=2))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")
