# Вариант 1
class Student:
    def __init__(self):
        self.name = "Roman"
        self.two_name = "Vladimir"
        self.model = self.Model()
        self.processor = self.Cpu()
        self.memory = self.Ram()

    def print_name(self):
        print(self.name, end="")

    class Model:
        def model(self):
            return "HP"

    class Cpu:
        def cpu(self):
            return "I7"

    class Ram:
        def memory(self):
            return 16


student = Student()
student_model = student.model
student_cpu = student.processor
student.memory = student.memory
print(f"{student.name} =>, {student_model.model()}, {student_cpu.cpu()}, {student.memory.memory()}")
print(f"{student.two_name} =>, {student_model.model()}, {student_cpu.cpu()}, {student.memory.memory()}")

print()


# Вариант 2
class Student:
    def __init__(self, name):
        self.name = name
        self.pc = self.Notebook()

    def print_name(self):
        print(self.name, end="")
        self.pc.show()

    class Notebook:
        def __init__(self):
            self.model = "Hp"
            self.processor = "I7"
            self.memory = 16

        def show(self):
            print(f"=> {self.model},{self.processor},{self.memory}")


p1 = Student("Roman")
p2 = Student("Vladimir")
p1.print_name()
p1.print_name()
