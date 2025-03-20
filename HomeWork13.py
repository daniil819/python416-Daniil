student = {}
col = int(input("Кол-во студентов:"))
sr = 0
for i in range(1, col + 1):
    name = input(str(i) + "-й студент:")
    ball = int(input("Балл:"))
    student[name] = ball
    sr += ball

average = sr / col
print(student)
print("Средний балл:", round(average), ". Студент с баллом выше среднего:")
for i in student:
    if student[i] > average:
        print(i)
