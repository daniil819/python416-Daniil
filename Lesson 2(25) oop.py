# 2 занятие задача на вывод данных
class Human:
    name = 'Daniil'
    birthday = '01.02.2006'
    phone = '00-00-00'
    country = 'Russia'
    city = "VRN"
    address = 'street, house'

    def print_info(self):
        print(" Персональные данные ".center(40, "*"))
        print(f"Имя: {self.name} \nДата рождения: {self.birthday} \nНомер телефон {self.phone} "
              f"\nСтрана: {self.country} \nГород: {self.city} \nДом-адрес: {self.address}")
        print("=" * 40)

    def input_info(self, first_name, birthday, phone, country, city, address):
        self.name = first_name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):  # устанавливаем новое имя
        self.name = name

    def get_name(self):  # получаем новое имя
        return self.name


h1 = Human()
h1.print_info()

h1.input_info("Юля", "23.05.1999", "8-800-355-35-35",
              "Россия", 'Воронеж', "Чистопрудный бульвар, 1А")
h1.print_info()

h1.set_name("Микаэлян")
h1.print_info()

print(h1.get_name())

# Задача 2 с новыми возможностями
# class Person:
#     skill = 10
#
#     # name = ""
#     # surname = ""
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name
#         self.surname = surname
#
#     def print_info(self, ):
#         # self.name = name
#         # self.surname = surname
#         print('Данные сотрудника:', self.name, self.surname)
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#     def add_skill(self, n):
#         self.skill += n
#         print("Квалификация", self.skill, "\n")
#
#
# p1 = Person("Антон", 'Мартынов')
# p1.print_info()
# p1.add_skill(3)
#
# del p1  # Удаляет переменную
#
# p2 = Person("Валентин", "Будэйко")
# p2.print_info()
# p2.add_skill(2)

# init
# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         self.count += 1
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.count)
# print(p1.count)

# Задача 3 подсчёт роботов
# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print("Робот выключается!", self.name)
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "Он был последним")
#         else:
#             print("Работающих осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Здорова! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("T-1000")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать любую работу\n")
# print("\nРоботы закончили работу. Выключай их.\n")
#
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)

# Private => self.__x
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if isinstance(x, int) or isinstance(x, float) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты неправильные")
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(5, "10")
# # print(p1.__dict__)
# # p1.z = 20
# # print(p1.__x, p1.__y)
# # p1.__x = 50
# # p1.__y = "abc"
# p1.set_coord("abc", 100)
# print(p1.get_coord_x())
# print(p1.get_coord_y())
# p1._Point__x = "abc"
# print(p1._Point__x)
# print(p1.__dict__)
