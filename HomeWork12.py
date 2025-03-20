sal = {'John':
           {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
       'Tom':
           {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
       'Anne':
           {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
       'Fionna': {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
       }
for x, y in sal.items():
    print(x)
    for i, j in y.items():
        print("\t", i, ": ", j, sep="")
user = input("Имя:")
reg = input("Регион:")
print(sal[user][reg])

new_base = int(input("Новое значение:"))
sal[user][reg] = new_base
print(sal[user])