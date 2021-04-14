from src.func import Square, Rectangle



squre = Square(3)
rectangle = Rectangle(2, 3)

def test_name():
    assert squre.name == 'Квадрат'

def test_angels():
    assert squre.angles == 4

def test_perimetr():
    assert squre.perimetr == 12


def test_area():
    assert squre.area == 9

def test_add_area():
    assert squre.add_area(rectangle) == 15