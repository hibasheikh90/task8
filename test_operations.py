import pytest
from operations import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(5, 0) == 0
    assert multiply(-2, 4) == -8

def test_divide():
    assert divide(6, 3) == 2.0
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
