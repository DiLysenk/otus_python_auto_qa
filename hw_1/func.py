import math


class Figure:

    def __repr__(self):
        pass


class Triangle(Figure):
    name = "Треугольник"
    angles = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        return math.sqrt(self.perimetr() *
                         (self.perimetr() - self.a) *
                         (self.perimetr() - self.b) *
                         (self.perimetr() - self.c)
                         )


class Rectangle(Figure):
    name = "Прямоугольник"
    angles = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b





class Square(Figure):
    name = "Квадрат"
    angles = 4

    def __init__(self, a):
        self.a = a

    def perimetr(self):
        return self.a * 4

    def area(self):
        return self.a * self.a




class Circle(Figure):
    name = "Круг"


    def __init__(self, r):
        self.r = r

    def perimetr(self):
        return 2 * 3.14 * self.r

    def area(self):
        return 3.14 * self.r ** 2


t = Triangle(3, 4, 6)
print(t.area())
print(t.perimetr())
print(t.name)
