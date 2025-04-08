import pytest


@pytest.mark.smoke
def test_one():
    print("biswanth")

@pytest.mark.regression
def test_two():
    print("pinnika")

@pytest.mark.regression
def test_three():
    print("My name is pinnika biswanth")