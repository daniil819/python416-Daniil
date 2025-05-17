# # Продолжение задачи
# import json
# from operator import index
#
# from HomeWork30 import student
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ""
#         # for i in self.marks:
#         #     st += str(i) + ", "
#         # return f"Студент => {self.name}: {self.marks}"
#         # st = ", ".join(map(str, self.marks))
#         # return f"Студент => {self.name}: {st}"
#         return f"Студент => {self.name}: {', '.join(map(str, self.marks))}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def get_file_name(self):
#         return self.name + ".json"
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open((self.get_file_name()), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n{st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         # st = gr1.remove_student(index)
#         # gr2.add_student(st)
#         gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + '.json'
#
#     def dump_to_json(self):
#         data = [
#             {"name": student.name, "marks": student.marks} for student in self.students
#         ]
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodhya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК python")
# # print(group1)
# # print()
# group1.add_student(st3)
# # print(group1)
# # print()
# group1.remove_student(1)
# print(group1)
# print()
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# print(group2)
# print()
# Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
#
# group2.dump_to_json()
# group2.load_from_file()
#
import csv
from asyncore import write

# Как ещё работает формат json
# Установка модулей
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(type(response.text))
# todos = json.loads(response.text)
# # print(type(todos[0]))
# # print(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
# max_complete = top_users[0][1]
# print(max_complete)  # 12
#
# users = []  # [5, 10]
# for user, num in top_users:
#     if num < max_complete:
#         break
#     users.append(str(user))
# print(users)
#
# max_users = " и ".join(users)
# print(max_users)
#
# print(f"Пользователи {max_users} выполнил {max_complete} задач")

# Формат CSV
# import csv
#
# with open("data1.csv") as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=';', fieldnames=file_names)
#     count = 0
#
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         else:
#             print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} годы.")
#         count += 1

# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саня", 5, 12])
#     writer.writerow(["Маша", 11, 17])

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]
with open('sw_data.csv', 'w') as f:
    writer = csv.writer(f, delimiter=";", lineterminator='\r')
    for row in data:
        writer.writerow(row)
with open('sw_data.csv', 'r') as f:
    print(f.read())
