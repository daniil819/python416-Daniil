# print("Проверка")
# print("Новое устройство")

# Работа с файлами

# f = open('text.txt')  # Относительный путь

# b = open(r'C:\Users\Garis mod\Desktop\Python\text.txt', "r")  # Абсолютный путь
# # print(*f)
# print(*b)
# print(f)
# print(f.mode)
# print(b.mode)

# print(f.name)
# print(b.name)
# print(b.encoding)
#
# b.close()
# print(b.closed)

# print(b.read(3))
# b.close()

#  Создание файла
# f = open("xyz.txt", 'w')
# f.write('This is line1. \n This is line2. \n This is line3. \n')
# f.close()

# Перенос строчек
# f = open('xyz.txt')
# print(f.read()
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())

# print(f.readlines(15))
# print(f.readlines())
# f.close()

# Прошли в цикле файл
# f = open('xyz.txt')
# for line in f:
#     print(line)
# f.close()


# Вносим элементы сами в файл
# lines = ["This is line1.\n", " This is line2.\n", "This is line3.\n"]
# f = open('lines.txt', 'w')
# f.writelines(lines)
# f.close()

# 2 способ через for
# Файлы работают только со строкой
# lines = [str(i) for i in range(10, 1000, 5)]
# print(lines)
#
# f = open("lines.txt", 'w')
# for index in lines:
#     f.write(index + "\t")
# f.close()

# Задача
file = "text2.txt"
f = open(file, 'w')
f.write('Замена строки в текстовом файле; \nизменить строку в списке; \nзаписать список в файл; \n')
f.close()

f = open(file, 'r')
read_line = f.readlines()
print(read_line)
read_line[1] = 'hello world'
print(read_line)
f.close()

f = open(file, 'w')
f.writelines(read_line)
f.close()

# Работа с курсором
# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возврощает текущую позицию условного курсора в файле
# print(f.seek(1))  # перемещает курсор на заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# Испытание других операторов
# f = open('text5.txt', 'a')
# print(f.write("I am learning python"))
# print(f.seek(0))
# print(f.write("--new string--"))
# # print(f.read())
# f.close()

# Открытие через with
# with open("text.txt", 'w') as f:
#     print(f.write('0123456789'))
# print(f.closed)

# Внесение данных через список
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# print(get_line(lst))
#
# with open("res.txt", 'w') as f:
#     f.write(get_line(lst))
# print("Конец программы")

# 2 часть
# with open('res.txt') as f:
#     nums = f.read()
#
# print(nums)
# print(sum(list(map(float, nums.split()))))
# print(sum(map(float, nums.split())))


# Задача
# with open('res2.txt', 'w') as f:
#     f.write('Файл — именованная область данных на носителе информации, используемая '
#             'как базовый объект  с данными в операционных системах.')  # `взаимодействия`
#
#
# def longest_words(file):
#     with open(file) as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("res2.txt"))


# Работа с несколькими файлами

# text = ('Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7'
#         '\nСтрока №8\nСтрока №9\nСтрока №10\n')
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# with open("one.txt", 'r') as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)

# Модуль OS
# import os

#
# print(os.getcwd())  # Путь к текущей директории
# print(os.listdir())  # Список папок, которые лежать в директории
# print(os.listdir(".."))
# print(os.listdir(".venv"))


# os.mkdir('folder.txt')  # Создание папки
# os.rmdir("folder.txt")  # удаление папки


# os.makedirs('nested1/nested2/nested3')  # Создаёт папку и в ней ещё папки

# os.remove("xyz.txt")  # Удалить файл
# os.rename('two.txt', "www.txt")  # Переименовали файл
# os.rename('www.txt', "folder/www.txt") # перемещение файла в папку
# os.rename('text5.txt', "nested1/nested2/nested3/text5.txt")
