# Исключения
# try: # попытаться
#     n = int(input("Введите число:"))
#     print(n * 2)
# except ValueError: # исключение
#     print("что-то пошло не так")
#
# print("код далее")

# 2 исключение
# try:
#     n = int(input("Введите делимое:"))
#     m = int(input("Введите делитель:"))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# запись нескольких исключение в одну строку
# try:
#     n = int(input("Введите делимое:"))
#     m = int(input("Введите делитель:"))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")


# Исключение с else и finally
# try:
#     n = int(input("Введите делимое:"))
#     m = int(input("Введите делитель:"))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")
# else:  # когда в блоке try не возникло исключение
#     print("Всё нормально. Вы ввели", n, "и", m)
# finally:  # выполниться в любом случае
#     print("Конец программы")

# Задача на конкатенацию данных
# 1 способ
# try:
#     n = input("Введите 1 число:")
#     m = input("Введите 2 число :")
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))

# 2 способ

# n = input("Введите 1 число:")
# m = input("Введите 2 число :")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#
# finally:
#     print(n + m)

# Работа с циклами
# while условие:
#     блок_кода


# Итерация - один проход цикла

# i = int(input("Введи:"))
# while i < 5:
#     print("i = ", i)
#     i += 1

# Вывод только чётных цифр
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# 2 вариант
# j = 2
# while j <= 20:
#     print(j, end="")
#     j += 2


# Задача
# n = int(input("Укажите кол-во символов:"))
# i = 0
# while i < n:
#     print("*", end=" ")
#     i += 1

#  2 способ
# n = int(input("Укажите кол-во символов"))
# print("*" * n)


# Написать программу, которая делает диапaзон и складывает все цифры
# a = int(input("Введите начало:"))
# b = int(input("Введите конец:"))
# res = 0
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print(res)

# Ввод целого числа с try и используем is not
# n = input("Введите целое число: ")
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError: (
#          print("Число не целое!"))
# n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# Бесконечный цикл continue
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue  # перебрасывает на проверку условия
#     print(i, end="")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл завершён")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# While True

# while True:
#     n = int(input("Введите положительное число:"))
#     if n < 0:
#         break

# Написать программу поиска произведения производительности чисел

# res = 1
# while True:
#     n = int(input("введите число:"))
#     if n == 0:
#         break
#     res = n * res
# print(res)
# print("\n Цикл завершён")

# i = 0
# while i < 10:
#     if i ==5:
#         break
#     print(i)
#     i+=1
# print("Цикл окончен i=", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1


# Таблица умножения

i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, "*", j, "=", i * j, end="\t\t")
        j += 1
    print()
    i += 1
