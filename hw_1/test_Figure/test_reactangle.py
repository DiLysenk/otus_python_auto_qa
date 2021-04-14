from src.func import Rectangle, Square


rectangle = Rectangle(2, 3)
square = Square(3)


def test_name():
    assert rectangle.name == 'Прямоугольник'

def test_angels():
    assert rectangle.angles == 4

def test_perimetr():
    assert rectangle.perimetr == 10


def test_area():
    assert rectangle.area == 6

def test_add_area():
    assert rectangle.add_area(square) == 15