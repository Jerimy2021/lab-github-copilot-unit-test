import pytest
from math_utils import generate_fibonacci, factorial, is_even

def test_generate_fibonacci():
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    with pytest.raises(ValueError, match="Input must be a non-negative integer."):
        generate_fibonacci(-1)

def test_factorial_utils():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-1)

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True
