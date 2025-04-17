# # Задача 2
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Иго!!рь', 'Николаевич']
#         # print(f)
#         if len(f) != 3:
#             raise TypeError("Неверный формат фио")
#         letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефисы")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 <= old <= 100:  # old < 14 or old > 100
#             raise TypeError("Возраст от 14 до 100")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("неверный формат")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 45, "1234 567890", 80.8)
# p1.fio = "Витёк жёсткий сигма"
# print(p1.__dict__)

# object
# class Point(object):
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# print(Point.__dict__)
# print(issubclass(Point, object))  # Являеться ли подклассом

# # Наследование
# class Point(object):
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x},{self.__y})"
#
#
# class Prop():
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределённый инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_rect(self):
#         print(f"Рисование Прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# # line = Line(Point(1, 2), Point(10, 20))  # Color и Width не передаём так как у них значение по умолчанию
# line = Line(Point(1, 0), Point(10, 20), "green", 5)
# line.draw_line()
#
# rect = Rect(Point(1, 2), Point(111, 1))
# rect.draw_rect()

# Наследование и дочерний
# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if isinstance(w, int) and w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Только положительные числа")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота только положительное число")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольник:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle("green", 10, 20)
# print(rect.area())
# print(rect.__dict__)

# Переопределение методов и дз на дом
# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class ReactFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()  # Получение метода из родительского класс если есть 2 одинаковых по имени функции
#         print("Фон:", self.fon)
#
#
# class ReactBorder(Rect):
#     ...
#
#
# shape1 = ReactFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = ReactBorder(345, 500, "1px", "solid", "red")
# shape2.show_rect()

# строка
# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегруз методами
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y=None):
        if y is None:
            self.x = x
        elif x is None:
            self.y = y
        else:
            self.x = x
            self.y = y


p1 = Point(5, 10)
print(p1.__dict__)
p1.set_coord(20, 30)
print(p1.__dict__)
p1.set_coord(50)
print(p1.__dict__)
