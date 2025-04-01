a = int(input("pos1 ="))
b = int(input("pos2 ="))
test = 'HomeWork 21-22.txt'
f = open(test, 'w')
f.write('Замена строки в текстовом файле; \nизменить строку в списке; \nзаписать список в файл; \n')
f.close()

f = open(test, 'r')
read_line = f.readlines()
print(read_line)
f.close()


if 0 <= a < len(read_line) and 0 <= b < len(read_line):
    read_line[a], read_line[b] = read_line[b], read_line[a]
    print(read_line)
    f.close()
else:
    print('Нету такого индекса')

f = open(test, 'w')
f.writelines(read_line)
f.close()
