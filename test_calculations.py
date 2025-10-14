
import pytest

from pytest_examples.my_calculations import Calculations


@pytest.fixture
def instance_input():
    calc = Calculations(6,2)
    return calc

def test_sum(instance_input):
    assert instance_input.find_sum() == 8

def test_diff(instance_input):
    assert instance_input.find_diff() == 4

def test_multiply(instance_input):
    assert instance_input.find_product() == 12

def test_division(instance_input):
    assert instance_input.find_quotient() == 3