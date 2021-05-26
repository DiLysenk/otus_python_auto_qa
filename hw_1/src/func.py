import math


class Figure:

    def __init__(self):
        self.area = self.area_s()

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            print('передан неправильный класс')

    def area_s(self):
        return self.area


class Triangle(Figure):
    name = "Треугольник"
    angles = 3

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.perimetr = self.a + self.b + self.c
        super().__init__() # тут я вызывал исполняемую функцию и родительского класса

    def area_s(self):
        return math.sqrt(self.perimetr * (self.perimetr - self.a) *
                         (self.perimetr - self.b) * (self.perimetr - self.c))


class Rectangle(Figure):
    name = "Прямоугольник"
    angles = 4

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        self.perimetr = (self.a + self.b) * 2
        super().__init__()


    def area_s(self):
        return self.a * self.b


class Square(Figure):
    name = "Квадрат"
    angles = 4

    def __init__(self, a):
        self.a = int(a)
        self.perimetr = self.a * 4
        super().__init__()

    def area_s(self):
        return self.a * self.a


class Circle(Figure):
    name = "Круг"
    angles = 0

    def __init__(self, r):
        self.r = int(r)
        self.perimetr = 2 * 3.14 * self.r
        super().__init__()

    def area_s(self):
        return 3.14 * (self.r ** 2)


c = Circle(4)
print(c.name)
