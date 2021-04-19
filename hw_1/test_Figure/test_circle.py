import pytest
from hw_1.src.func import Square

square = Square(3)

@pytest.mark.parametrize('r', ('3'))
def test_name(circle, r):
    assert circle.name == 'Круг'

@pytest.mark.parametrize('r', ('3'))
def test_angels(circle, r):
    assert circle.angles == 0

@pytest.mark.parametrize('r', ('3'))
def test_perimetr(circle, r):
    assert circle.perimetr == 18.84

@pytest.mark.parametrize('r', ('3'))
def test_area(circle, r):
    assert circle.area == 28.26

@pytest.mark.parametrize('r', ('3'))
def test_add_area(circle, r):
    assert circle.add_area(square) == 37.260000000000005