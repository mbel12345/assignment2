""" tests/test_operations.py """
import pytest

from app.operations import addition, division, multiplication, subtraction

# 3x3 = 9 cases for each non-division function, since each of the two inputs can be either 0, positive, or negative.
# For division, there are 6 test cases, with the 3 division by 0 cases being put into their own test case.

def test_addition():

    # Addition test cases
    assert addition(2, 5) == 7
    assert addition(1, -4) == -3
    assert addition(-5, 10) == 5
    assert addition(-3, -4) == -7
    assert addition(0, 0) == 0
    assert addition(0, -4) == -4
    assert addition(-5, 0) == -5
    assert addition(0, 4) == 4
    assert addition(6, 0) == 6

def test_subtraction():

    # Subtraction test cases
    assert subtraction(2, 5) == -3
    assert subtraction(1, -4) == 5
    assert subtraction(-5, 10) == -15
    assert subtraction(-3, -4) == 1
    assert subtraction(0, 0) == 0
    assert subtraction(0, -4) == 4
    assert subtraction(-5, 0) == -5
    assert subtraction(0, 4) == -4
    assert subtraction(6, 0) == 6

def test_multiplication():

     # Multiplication test cases
    assert multiplication(2, 5) == 10
    assert multiplication(1, -4) == -4
    assert multiplication(-5, 10) == -50
    assert multiplication(-3, -4) == 12
    assert multiplication(0, 0) == 0
    assert multiplication(0, -4) == 0
    assert multiplication(-5, 0) == 0
    assert multiplication(0, 4) == 0
    assert multiplication(6, 0) == 0

def test_division_valid():

    # Division test cases for valid (i.e. non-0) inputs
    assert division(2, 5) == 0.4
    assert division(1, -4) == -0.25
    assert division(-5, 10) == -0.5
    assert division(-3, -4) == 0.75
    assert division(0, -4) == 0
    assert division(0, 4) == 0

def test_division_by_zero_error():

    # Check that error is raised when user enters 0 as the second number
    for combo in [
        (0, 0),
        (-5, 0),
        (6, 0),
    ]:
        with pytest.raises(ValueError, match='Division by zero is not allowed.'):
            division(combo[0], combo[1])
