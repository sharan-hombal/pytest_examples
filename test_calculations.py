
import pytest

from pytest_examples.my_calculations import Calculations


@pytest.fixture
def instance_input():
    calc = Calculations(6,4)
    return calc

def test_sum(instance_input):
    assert instance_input.find_sum() == 10

def test_diff(instance_input):
    assert instance_input.find_diff() == 2

def test_multiply(instance_input):
    assert instance_input.find_product() == 24

def test_division(instance_input):
    assert instance_input.find_quotient() == 2  # expected to fail