import math


class Figure:

    def __init__(self):
        self.area = 0


    def add_area(self, figure):
        if isinstance(self, Figure):
            return self.area + figure.area
        else:
            print('передан неправильный класс')


class Triangle(Figure):
    name = "Треугольник"
    angles = 3


    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.perimetr = self.a + self.b + self.c
        self.area = math.sqrt(self.perimetr * (self.perimetr - self.a) *
                              (self.perimetr - self.b) * (self.perimetr - self.c))



class Rectangle(Figure):
    name = "Прямоугольник"
    angles = 4

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.perimetr = (self.a + self.b) * 2
        self.area = self.a * self.b


class Square(Figure):
    name = "Квадрат"
    angles = 4

    def __init__(self, a):
        super().__init__()
        self.a = a
        self.perimetr = self.a * 4
        self.area = self.a * self.a


class Circle(Figure):
    name = "Круг"
    angles = 0

    def __init__(self, r):
        super().__init__()
        self.r = r
        self.perimetr = 2 * 3.14 * self.r
        self.area = 3.14 * (self.r ** 2)


s = Square(3)
t = Triangle(2, 3, 4)
print(s.area)
print(t.area)
print(type(t.add_area(s)), "----", t.add_area(s))
