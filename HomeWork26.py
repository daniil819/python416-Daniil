import math


class Math:
    count = 0

    @staticmethod
    def formula(a, b, c):
        Math.count += 1
        p = (a + b + c) // 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def width_base(a, b):
        Math.count += 1
        return (a * b) // 2

    @staticmethod
    def square(a):
        Math.count += 1
        return a ** 2

    @staticmethod
    def base_rectangle(a, b):
        Math.count += 1
        return a * b

    @staticmethod
    def counter():
        return Math.count


print("Треугольник по формуле Герона (3, 4, 5):", Math.formula(3, 4, 5))
print("Площадь треугольника через высоту и основание (6, 7):", Math.width_base(6, 7))
print("Площадь квадрата (7):", Math.square(7))
print("Площадь прямоугольника (2, 6):", Math.base_rectangle(2, 6))
print("Кол-во подсчётов:", Math.counter())
