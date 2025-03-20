a = [int(input("->")) for i in range(int(input("Введите числа для списка:")))]
sum = 0
for i in range(len(a)):
    if a[i] < 0:
        sum += a[i]
print("Сумма нечётных чисел:", sum)
