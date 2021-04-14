from src.func import Square, Circle



squre = Square(3)
circle = Circle(3)

def test_name():
    assert circle.name == 'Круг'

def test_angels():
    assert circle.angles == 0

def test_perimetr():
    assert circle.perimetr == 18.84


def test_area():
    assert circle.area == 28.26

def test_add_area():
    assert circle.add_area(squre) == 37.260000000000005