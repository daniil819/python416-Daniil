# Модуль ос
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

# 2 часть занятия
# import os
#
# # print(os.walk('nested1'))
# for root, dirs, files in os.walk('nested1', topdown=False):  # Проверяем папку на файлы
#     print("Root:", root)
#     print("\tdirs:", dirs)
#     print("\tFiles:", files)


# Подмодуль os.path
# import os.path
#
# print(os.path.split(r"C:\Users\Garis mod\Desktop\Python\nested1\nested2\nested3\text4.txt"))
#
# print(os.path.join(r'C:\Users', "Desktop", "Garis mod", "nested3", "nested2", "text4.txt"))  # собирает путь из кусков

# Задача на создание дерева
# import os
#
# dirs = [r"Work\F1", r"Work\F2\F21"]
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for d, files in files.items():
#     for file in files:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, 'w').close()
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"такой-то текст {file}")
#
#
# def print_three(root, topdown):
#     print(f'Обход {root} {"Сверху вниз" if topdown else "снизу вверх"}')
#     for root, directory, file_name in os.walk(root, topdown):
#         print(root)
#         print(directory)
#         print(file_name)
#     print('-' * 50)
#
#
# print_three("Work", False)
# print_three("Work", True)


# проверка существование пути
# import os
# import time

# print(os.path.exists(r"C:\Users\Garis mod\Desktop\Python\nested1\nested2\nested3\text4.txt"))  # Существует ли путь
# print(os.path.isfile(r"C:\Users\Garis mod\Desktop\Python\nested1\nested2\nested3"))  # папка или файл
# print(os.path.isdir(r"C:\Users\Garis mod\Desktop\
# Python\nested1\nested2\nested3"))  # являеться ли последний элемент паппкой
#
# print(os.path.getsize(r"C:\Users\Garis mod\Desktop\Python\nested1\nested2\nested3\text4.txt"))  # Смотрим размер файла


# file = "readme.txt"
# print(os.path.getsize(file))  # размер в байтах
# print(os.path.getatime(file))  # время последнего доступа
# print(os.path.getmtime(file))  # время последнего изменения
# print(os.path.getctime(file))  # время создание файла
#
# kb = os.path.getsize(file)
# a = os.path.getatime(file)
# m = os.path.getmtime(file)
# c = os.path.getctime(file)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# print(kb // 1024)



