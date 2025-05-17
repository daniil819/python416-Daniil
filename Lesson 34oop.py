# Упаковка и распаковка данных
# import pickle
#
# file_name = "basket.txt"
# shop_list = {
#     "Фрукты": ["Яблоки", "Лимон"],
#     "Овощи": ["морковь", "лук"],
#     "Бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)
import json
import pickle
from tkinter.font import names


# Задание
# import pickle
#
#
# class Test:
#     num = 25
#     st = "hi"
#     lst = [1, 2, 3]
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)
# string = pickle.dumps(obj)
# print(string)
# string2 = pickle.loads(string)
# print(string2)

# Что можно сохранить
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr["c"]
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3.__dict__)

# Модуль Json
# import json
#
# data = {
#     "name": "Olga",
#     'age': 35,
#     20: None,
#     None: "no",
#     True: False,
#     'hobbies': ("running", 'signing'),
#     'children': [
#         {
#             "firstName": "Alice",
#             'age': 6
#         }
#     ]
# }
#
# # with open("data_file.json", "w") as f:
# #     json.dump(data, f, indent=4)
# # with open("data_file.json", "w") as f:
# #     data1 = json.load(f)
# #
# # print(data1)
#
# string = json.dumps(data)
# print(string, type(string))
# data1 = json.loads(string)
# print(data1)

# Русские слова
# import json
#
# x = {"name": "Виктор"}
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
#
# st = json.dumps(x)
# print(json.loads(st))

# Функция генерации персональных данных
# Дз
# import json
# from random import choice
#
#
# def gen_person():
#     name = ""
#     tel = ""
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#     while len(tel) != 10:
#         tel += choice(nums)
#     person = {
#         "name": name,
#         "tel": tel,
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#     data.append(person_dict)
#
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

# Задача
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # st = ""
        # for i in self.marks:
        #     st += str(i) + ", "
        # return f"Студент => {self.name}: {self.marks}"
        # st = ", ".join(map(str, self.marks))
        # return f"Студент => {self.name}: {st}"
        return f"Студент => {self.name}: {', '.join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def get_file_name(self):
        return self.name + ".json"

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open((self.get_file_name()), "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))


class Group:
    def __init__(self, students):
        self.students = students

    def __str__(self):
        st = "\n".join(map(str, self.students))
        return f"{st}"
    

st1 = Student("Bodhya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
sts1 = [st1, st2]
group1 = Group(sts1)
print(group1)
print(st1)
st1.add_mark(4)
print(st1)
st1.delete_mark(2)
print(st1)
st1.edit_mark(4, 4)
print(st1)
print(st1.average_mark())
st1.dump_to_json()
st1.load_from_file()
