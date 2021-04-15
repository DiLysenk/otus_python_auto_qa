import pytest
from hw_1.src.func import Square

square = Square(3)

@pytest.mark.parametrize('a, b, c', [('2', '3', '4')])
def test_name(triangle, a, b, c):
    assert triangle.name == 'Треугольник'

@pytest.mark.parametrize('a, b, c', [('2', '3', '4')])
def test_angels(triangle, a, b, c):
    assert triangle.angles == 3

@pytest.mark.parametrize('a, b, c', [('2', '3', '4')])
def test_perimetr(triangle, a, b, c):
    assert triangle.perimetr == 9

@pytest.mark.parametrize('a, b, c', [('2', '3', '4')])
def test_area(triangle, a, b, c):
    assert triangle.area == 43.474130238568314

@pytest.mark.parametrize('a, b, c', [('2', '3', '4')])
def test_add_area(triangle, a, b, c):
    assert triangle.add_area(square) == 52.474130238568314