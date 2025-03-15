import pytest
from calculator import *

class TestCalculator():

    fullRegressionOnly = False
    
    def setup_class(self):
        print("\nSetup executado uma única vez para toda a classe!")
    
    def teardown_class(self):
        print("\nTeardown executado uma única vez para toda a classe!")
    
    def setup_method(self, method):
        print(f"\nPreparando teste {method.__name__}")
    
    def teardown_method(self, method):
        print(f"\nCleanup do teste {method.__name__}")
    
    @pytest.mark.parametrize("expression, expected", [
        ("3+5", 8),
        ("10-2", 8),
        ("4*5", 20),
        ("20/4", 5),
        ("2^3", 8),
        ("2**4", 16),
        ("5!", 120),
        ("v9", 3),
        ("log(1)", 0),
        ("2*log(100)", 4),
        ("(3+2)*2", 10),
        ("-2 -4", -6)
    ])
    
    def test_evaluate_expression(self, expression, expected):
        assert evaluate_expression(expression) == expected
    
    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            evaluate_expression("10/0")
    
    def test_negative_square_root(self):
        with pytest.raises(ValueError):
            evaluate_expression("v(-4)")
    
    def test_invalid_input(self):
        with pytest.raises(ValueError):
            evaluate_expression("3 + @")
    
    def test_factorial(self):
        assert factorial(5) == 120
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_log(self):
        assert log(100) == 2
        assert log(1) == 0
        assert pytest.approx(log(10)) == 1

    def test_power(self):
        assert power(2, 3) == 8
        assert power(10, 2) == 100
        assert power(2, 0) == 1

    def test_division(self):
        assert division(10, 2) == 5
        assert division(9, 3) == 3
        with pytest.raises(ZeroDivisionError):
            division(10, 0)

    def test_sum(self):
        assert sum(3, 5) == 8
        assert sum(-1, 1) == 0

    def test_sub(self):
        assert sub(10, 2) == 8
        assert sub(2, 10) == -8

    def test_multiplication(self):
        assert multiplication(4, 5) == 20
        assert multiplication(-1, 5) == -5

    def test_square_root(self):
        assert square_root(9) == 3
        assert square_root(0) == 0
        with pytest.raises(ValueError):
            square_root(-1)