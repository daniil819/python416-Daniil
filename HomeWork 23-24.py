import os

# В папке nested 3 находятся: text3.txt, text4.txt
search_file = input('Введите имя файла для папки nested3:')
file = r"C:\Users\Garis mod\Desktop\Python\nested1\nested2\nested3"
for root, dirs, files in os.walk(file, topdown=False):
    if search_file in files:
        # b = os.path.getatime(file)
        print(f"{os.path.split(file)[1]}/{search_file}", "-", 'last time', os.path.getatime(file), "sec")
    else:
        print('Нету такого файл')
