import math

# print('Выберите фигуру')
mat = int(input("\n1-треугольник\n2-прямоугольник\n3-круг\nВыберите фигуру:"))
ot = 0
if mat == 1:
    a = int(input('Введите основание:'))
    h = int(input('Введите высоту:'))
    ot = (a * h) / 2
elif mat == 2:
    a = int(input('Введите длину:'))
    b = int(input('Введите ширину:'))
    ot = a * b
elif mat == 3:
    a = int(input('Введите радиус:'))
    ot = math.pi * a ** 2
else:
    print("Некорректное значение")
print("Ответ:", round(ot, 2))
