# логические операторы
# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True = True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False = True
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True = True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False = True
#
# print(not 9 - 5)
# print(not 7 - 7)


# условие if

# cnt = 5
# if cnt < 10:
#     # cnt = cnt + 1 # более длинный оператор
#     cnt += 1
#     print(cnt)


# Пример введите свой возраст с else
# age = int(input("Введите свой возраст:"))
# if age >= 18:
#     print("Доступ разрешён")
# else:
#     print("Доступ не разрешён")

# elif
# a = int(input("a:"))
# b = int(input("b:"))
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")


# Задача на проверку

# a = int(input("Первая сторона:"))
# b = int(input("Вторая сторона:"))
# c = int(input("Третья сторона:"))
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or b == c or c == a:
#     print("Равнобедренный")
# else:
#     print("Равносторонний ")


# Дни недели
# day = int(input("Введите день недели цифрами:"))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Нету такого дня")


# Дни лето
# a = int(input("Введите номер месяца:"))
# if a == 12 or a == 1 or a == 2:
#     print("Зима")
# elif a == 3 or a == 4 or a == 5:
#     print("Весна")
# elif a == 6 or a == 7 or a == 8:
#     print("Лето")
# elif a == 9 or a == 10 or a == 11:
#     print("Ocень")
# else:
#     print("Нету таких месяцев")

# 2 способ
# season = int(input("Введите номер месяца: "))
# print("Время года: ", end="")
# if 1 <= season <= 12:
#     print("Зима")
#     if 1 <= season <= 2 or season == 12:
#         print("Весна")
#     if 3 <= season <= 5:
#         print("Лето")
#     if 6 <= season <= 8:
#         print("Осень")
#     if 9 <= season <= 11:
#     else:
#         print("Такого месяца нет")


# pass - заглушка для временного способа, чтобы не показывал ошибку можно ещё (...)
# Написать программу про ворон с диапазоном
# n = int(input("Введите кол-во ворон:"))
# if 0 <= n <= 9:
#     print("На ветке", end="")
#     if n == 1:
#         print("", n, "ворона")
#     if 2 <= n <= 4:
#         print("", n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print("", n, "ворон")
# else:
#     print("Ошибка ввода")


# Switch
# password = "admin"
#
# match password:
#     case "admin":
#         print("Админ")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")


# day = 'понедельник'
# time = 15
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# Тернарное выражение
a, b = 30, 20
print(a if a < b else b)
