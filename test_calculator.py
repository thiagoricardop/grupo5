import pytest
from calculator import *


def test_log():
    assert log(10) == 2.302585092994046

@pytest.mark.parametrize(("a", "expected"), 
                         [(1, 1), (5, 120)])
def test_factorial(a, expected):
    assert factorial(a) == expected