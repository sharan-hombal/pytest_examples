import pytest
'''
sometimes we need may need to skip the test for some reasons then

@pytest.mark.xfail -> Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests. 
Details of these tests will not be printed even if the test fails

@pytest.mark.skip -> Skipping a test means that the test will not be executed. 
'''

@pytest.mark.xfail
def test_addition():
    assert (1 + 1) == 4

@pytest.mark.skip
def test_subtraction():
    assert (1 - 2) == 3

def test_multiplication():
    assert (2 * 2) == 4


'''
skip_xfail_examples.py::test_addition XFAIL                                                                                                          [ 33%]
skip_xfail_examples.py::test_subtraction SKIPPED (unconditional skip)                                                                                [ 66%]
skip_xfail_examples.py::test_multiplication PASSED                                                                                                   [100%]

========================================================= 1 passed, 1 skipped, 1 xfailed in 0.05s =========================================================

'''