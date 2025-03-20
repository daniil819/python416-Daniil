# print("Строка \
# символов")
#
# print('строка \n символов') #Перенос на другую строку \n
#
# print("Документ \"file.txt\"") #Экранирование строки
#
# print("\tДокумент \"file.txt\"     находиться   по пути: \rD\\folder\\file.txt")


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3 * 3)

# Операторы математики
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 4)
# print(6 // 4)
# print(6 ** 4)
# print(6 % 4)

# Нахождение суммы
# a = 5
# b = 7
# c = 3
# print("Сумма:", a + b+ c)
# print("Произведение:", a * b* c)
# print("Среднее арифметическое:", (a + b + c )/ 3)

# 2 способ через переменную res
# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("Сумма:", a + b + c)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", res / 3)

# += Примеры
# num = 10
# num +=5
# print(num)
# num -=3
# print(num)
# num *=4
# print(num)
# num **=2
# print(num)

# развернуть числа
# num = 4321
# print(num)
# a = num % 10
# print("a:", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)

# # 2 cпособ
# num = 4321
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)

# Преобразование
# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)

# int , round - округление
# print(int(3.8))
# print(round(3.8))
# print(type(int(3.8)))
# print(round(3.895, 2)) #2- это сколько символов после строчки, мы хотим видеть
# print(type(round(3.895, 2)))

#  преобразование чисел с плавающей запятой FLOAT
# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# Как работает функции print
# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, "лет.", sep="", end="")  # sep - можно поставить любой символ
# # #end -чем кончается строка
# print("Новая строка")

# input
# name = input("Введите имя:")
# print("Ваше имя:", name)

# num = int(input("Введите число:"))
# power = int(input("Введите степень:"))
# res = num ** power
# print("число:",num, "степень:",power, "итог:", res )

# Задача
# one = int(input("Введите 1 число:"))
# two = int(input("Введите 2 число:"))
# three = int(input("Введите 3 число:"))
# four = int(input("Введите 4 число:"))
# one_res = one + two
# two_res =  three + four
# res = one_res / two_res
# print("Результат", round(res, 2 ) )

# Булевы значения
# b1 = True
# b2 = False
# print(type(b1))
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))
# print(bool(" "))
# print(bool(5))
# print(bool(0))
# print(bool(0.1))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
# a = None
# print(a)
# print(type(a))

# Cравнение чисел
# print(7 == 7)
# print (2 + 5 == 7/3)
# print(2 + 5 != 7 / 3)
# print(8 > 8)
# print(8 > 5)
# print(8 >= 8)
# print("python">"Python") #из за кодировки символов ASCII


# print(2 < 4 < 9)  # True && True => True
# print(2 * 5 > 7 >= 4 + 3)
# # 10 > 7 >= 7  True && True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False && True =>
# a = "10"
# b = 10
# c = a == b
# print(a, b, c)
