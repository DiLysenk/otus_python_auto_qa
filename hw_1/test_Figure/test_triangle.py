from src.func import Triangle, Square


triangle = Triangle(2, 3, 4)
square = Square(3)


def test_name():
    assert triangle.name == 'Треугольник'

def test_angels():
    assert triangle.angles == 3

def test_perimetr():
    assert triangle.perimetr == 9


def test_area():
    assert triangle.area == 43.474130238568314

def test_add_area():
    assert triangle.add_area(square) == 52.474130238568314