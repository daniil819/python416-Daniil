import math

# 1 Вариант
circle = ((lambda r: math.pi * r ** 2)(2))
print('Площадь окружности радиуса 2:', circle)
rec = ((lambda a, b: a * b)(10, 13))
print("Площадь прямоугольник размером 10 * 13:", rec)
trap = ((lambda a, b, h: ((a + b) * h) / 2)(7, 5, 3))
print('Площадь трапеции для a=7, b=5, h=3:', trap)

# 2 Вариант
area = {
    'circle': lambda r: math.pi * r ** 2,
    'rec': lambda a, b: a * b,
    'trap': lambda a, b, h: (a + b) * h / 2
}
print(area['circle'](2))
print(area['rec'](10, 13))
print(area['trap'](7, 5, 3))
