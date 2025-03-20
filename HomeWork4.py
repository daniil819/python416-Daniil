n = int(input("Укажите кол-во символов: "))
a = int(input("0 - горизонтальная  1 - вертикальная: "))
symbol = input("Тип символа:")
i = 0

while i < n:
    if a == 0:
        print(symbol, end=" ")
    elif a == 1:
        print(symbol)
    i += 1

