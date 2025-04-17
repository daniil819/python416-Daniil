class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def show_rect(self):
        print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")


class ReactFon(Rect):
    def __init__(self, width, height, background):
        super().__init__(width, height)
        self.fon = background

    def show_rect(self):
        super().show_rect()
        print("Фон:", self.fon)


class ReactBorder(Rect):
    def __init__(self, width, height, frame, type_frame, color_frame):
        super().__init__(width, height)
        self.frame = frame
        self.type_frame = type_frame
        self.color_frame = color_frame

    def show_rect(self):
        super().show_rect()
        print(f"Ширина рамки: {self.frame}\nТип рамки:{self.type_frame}\nЦвет рамки: {self.color_frame}")


shape1 = ReactFon(400, 200, "yellow")
shape1.show_rect()
print()
shape2 = ReactBorder(600, 300, "1px", "solid", "red")
shape2.show_rect()


