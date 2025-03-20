num = int(input("Введите пятизначное число:"))
print("Число:", num)

temp_one = num

res_one = temp_one % 10 * 1
temp_one //= 10
res_one *= temp_one % 10 * 1
temp_one //= 10
res_one *= temp_one % 10 * 1
temp_one //= 10
res_one *= temp_one % 10 * 1
temp_one //= 10
res_one *= temp_one % 10 * 1
temp_one //= 10
print("Произведение цифр числа:", res_one)

temp = num
res_two = 0

res_two += temp % 10 * 1
temp //= 10
res_two += temp % 10 * 1
temp //= 10
res_two += temp % 10 * 1
temp //= 10
res_two += temp % 10 * 1
temp //= 10
res_two += temp % 10 * 1
temp //= 10

print("Среднее арифметическое:", res_two // 5)
