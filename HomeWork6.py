a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []
print(a)
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end=" ")
