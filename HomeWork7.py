import random

a = [random.randint(0, 100) for i in range(10)]
print(a)
lst = a.copy()
a.sort()
minimum = a[0]
# for i in range(len(a)):
#     if a[i] < minimum:
#         minimum = a[i]
print('Min:', minimum)

# if minimum in a:
ind = lst.index(minimum)
print('Index min:', ind)
print('Итог:', lst[ind:])
