a = set(input("Введите первую строку: "))
b = set(input("Введите вторую строку: "))
s = a.difference(b)
print(tuple(s))
