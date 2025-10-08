import pytest

'''
Fixtures are functions, which will run before each test function to which it is applied. 
Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data.
'''
@pytest.fixture
def input_value():
    return 10

def test_divide_by_2(input_value):
    assert input_value % 2 == 0

def test_divide_by_3(input_value):
    assert input_value % 3 == 0


