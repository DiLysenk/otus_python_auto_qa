import pytest
from hw_1.src.func import Circle, Rectangle, Square, Triangle

@pytest.fixture
def circle(r):
    return Circle(r)


@pytest.fixture
def square(a):
    return Square(a)

@pytest.fixture
def triangle(a, b, c):
    return Triangle(a, b, c)


@pytest.fixture
def rectangle(a, b):
    return Rectangle(a, b)