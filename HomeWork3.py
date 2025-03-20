n = int(input("Введите число от 1-99:"))
two = n
if 11 <= two <= 14:
    print(n, "копеек")
elif 1 <= two <= 10 or 15 <= two <= 99:
    two = two % 10
    if two == 1:
        print(n, "копейка")
    elif 2 <= two <= 4:
        print(n, "копейки")
    else:
        print(n, "копеек")
else:
    print("введите числа из указанного диапазона")
