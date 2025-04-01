# КАК СОЗДАЁТЬСЯ КЛАСС и методы и свойства
# class Point:
#     x = 1  # Свойства
#     y = 2  # Свойства
#
#
# p1 = Point()  # Создали экземпляр(обьект) класса
# p1.x = 10  # Поменяли значение свойства
# p1.y = 20
# # Point.x = 100  # изменение значение свойства для всех экземпляров
#
# print(p1.x)  # Обратились к x через экземпляр класса
# print(p1.y)  # Обратились к y через экземпляр класса
# print(p1.__dict__)  # Показывает свойства экземпляров класса для p1
#
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)  # Покажет пустой словарь так как покажет свойства именно для p2
#
# print(Point.__dict__)  # Покажет свойства класса

# СОЗДАНИЕ МЕТОДА
# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):  # Метод
#         self.x = x1
#         self.y = y1
#     # print(self.__dict__)
#     # print("Устанавливаем координаты")
#
#
# p1 = Point()
# print(type(p1))
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)  # Вызов класса 1 вариант
# print(p1.__dict__)
# Point.set_coord(p1, 20, 30)  # Вызов класса 2 вариант
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coord(100, 200)
# print(p2.__dict__)

# ДОКУМЕНТАЦИЯ
class Point:
    """Класс предоставление координат точек на плоскости"""
    x = 1
    y = 2

    def set_coord(self, x1, y1):
        self.x = x1
        self.y = y1


p1 = Point()
print(Point.__doc__)
print(Point.__dict__)
