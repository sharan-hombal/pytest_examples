import pytest

"""
Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker −

@pytest.mark.parametrize
"""

@pytest.mark.parametrize("num1, num2, expected", [(1,1,1), (2,2,4), (3,4,12), (2,6,12), (4,4,16)])
def test_multiplication(num1, num2, expected):
    assert num1 * num2 == expected