import pytest
import pylint

def capital_case(x):
    return x.capitalize()

def multiply_two(y):
    return y * 2

# Tests

def test_capital_case():
    assert capital_case('test') == 'Test'

def test_multiply_two():
    assert multiply_two(2) == 4
    assert multiply_two(4) == 8
    assert multiply_two(8) == 16
