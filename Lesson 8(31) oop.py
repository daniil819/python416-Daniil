class Student:
    def __init__(self, name, *marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            return IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым - положительным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value


s1 = Student("Сергей", 5, 5, 3, 4, 5)
# print(s1.marks[2])
print(s1[2])
s1[10] = 4
print(s1.marks)
