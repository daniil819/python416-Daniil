# Глобальная переменная
# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)

# Нелокальная
def outer(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        s += i * j

    inner(a, b)
    inner(a, c)
    inner(b, c)
    s = 2 * s
    return s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))
