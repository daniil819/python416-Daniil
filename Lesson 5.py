# FOR
# for element in collections
#     print(element)


# for i in "Hello", "world":  # ВЫВЕЛ ПРЕДЛОЖЕНИЕ
#
# for i in "Hello":  # РАЗБИЛ ПО ОДНОМУ СИМВОЛУ
#     print(i)


# Range (start, stop, step)

# for i in range(1, 10, 2):  # 1 - начало(start); 10 - (stop) считает до числа не включая его; 2 - шаг (step)
#     print(i, end=" ")

# РАЗЛИЧИЕ while и for

# ЗАДАЧА НА ВВОД ЦЕЛОГО ЧИСЛА НА КОТОРОЕ ОНО ДЕЛИТЬСЯ БЕЗ ОСТАТКА

# number = int(input("Введите число:"))
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i, end=" ")

# Вывод однинаковых чисел из диапазона от 10-100

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# print('\n2 способ')
# for i in range(11, 100, 11):
#     print(i, end=" ")

# else и for
# for i in range(12):
#     if i == 1:
#         break
#     print(i)
# else:
#     print("Конец")


# Вложенный цикл в for
# for i in range(3):  # for(i = 0; i < 3; i++) как JS цикл отрабатывает до 3 раз
#     print("+++")
#     for j in range(2):  # for(j = 0; j < 2; j++)
#         print("---")


# # Задание вывод прямоугольник из *
#
# w = int(input("Введите длину:"))
# h = int(input("Введите высоту:"))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()  # Перенос на другую строку

# Задание вывод прямоугольник из * и внутри пустой

# w = int(input("Введите длину:"))
# h = int(input("Введите высоту:"))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# for в одну строку
# string = [letter * 2 for letter in "python"]
# print(string)
#
# for letter in "python":
#     print(letter * 2, end="\t")


# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end="\t")


# СПИСКИ (LIST)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list([8, 2, 3, 5, 6, 9])
# print(num1)


# Отчёт от отрицательного занчения
# nums = [3, 2, 8, 7, 4, 5, 0, "one", True]
#  print(nums[4])
#  print(nums[2])
#  print(nums[-1])

# Изменение значений
# nums = [8, 7, 9, 3, 4, 2]
# print(nums)
# nums[2] = 444
# print(nums)
# nums[-1] += 2
# print(nums)


# nums = [9, 8, 7, 6, 5, 4]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print("Длина списка:", len(nums))


# # Что можно делать со списками
# # Сложение списков
# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
#

# # Увеличeть повтор списка умножением
# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# print(n * 3)

# перевод каких либо типов в списки
# print(list("Hello"))
#
# print(range(10))
# print(list(range(10)))
# print(list(range(10, 2, -2)))


# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)  # 0,0,0,0,0

# a = [i ** 2 for i in range(1, 5)]
# print(a)  # [1, 4, 9, 16]

# Пользователь вводит значение списка
# a = [0] * int(input("Введите кол-во элементов списка-"))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# в одну строку
a = [int(input("->")) for i in range(int(input("n =")))]
print(a)
