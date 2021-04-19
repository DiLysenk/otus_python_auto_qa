import pytest
from hw_1.src.func import Square

square = Square(3)

@pytest.mark.parametrize('a, b', [('2', '3'),
                         ('4', '9')])
def test_name(rectangle, a, b):
    assert rectangle.name == 'Прямоугольник'


@pytest.mark.parametrize('a, b', [('2', '3')])
def test_angels(rectangle, a, b):
    assert rectangle.angles == 4

@pytest.mark.parametrize('a, b', [('2', '3')])
def test_perimetr(rectangle, a, b):
    assert rectangle.perimetr == 10

@pytest.mark.parametrize('a, b', [('2', '3')])
def test_area(rectangle, a, b):
    assert rectangle.area == 6

@pytest.mark.parametrize('a, b', [('2', '3')])
def test_add_area(rectangle, a, b):
    assert rectangle.add_area(square) == 15