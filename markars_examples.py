
import pytest

'''
markers are used to group the tests which are to be run
To run all 'airthematic' tests run:
pytest -m airthematic markers_examples.py -v

To run all 'other' tests run:
pytest -m other markers_examples.py -v

'''
@pytest.mark.airthematic
def test_addition():
    assert (3+1) == 4

@pytest.mark.airthematic
def test_subtraction():
    assert (3-1) == 4

@pytest.mark.airthematic
def test_multiplication():
    assert (2*3) == 6

@pytest.mark.other
def test_compare():
    assert "sharan" == "sharan"
