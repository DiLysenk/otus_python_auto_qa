import pytest
from hw_1.src.func import Rectangle

rectangle = Rectangle(2, 3)

@pytest.mark.parametrize('a', ('3'))
def test_name(square, a):
    assert square.name == 'Квадрат'

@pytest.mark.parametrize('a', ('3'))
def test_angels(square, a):
    assert square.angles == 4

@pytest.mark.parametrize('a', ('3'))
def test_perimetr(square, a):
    assert square.perimetr == 12

@pytest.mark.parametrize('a', ('3'))
def test_area(square, a):
    assert square.area == 9

@pytest.mark.parametrize('a', ('3'))
def test_add_area(square, a):
    assert square.add_area(rectangle) == 15