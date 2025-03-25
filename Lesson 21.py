# print("Проверка")
# print("Новое устройство")

# Работа с файлами

# f = open('text.txt') # Относительный путь

b = open(r'C:\Users\Garis mod\Desktop\Python\text.txt', "r")  # Абсолютный путь
# print(*f)
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

print(b.read(3))
b.close()