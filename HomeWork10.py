import random


def number(a, b):
    return tuple(random.randint(a, b) for i in range(10))


a = number(0, 5)
print(a)
b = number(-5, 0)
print(b)
j = (a + b)
print(j)
print("0 =", j.count(0))
