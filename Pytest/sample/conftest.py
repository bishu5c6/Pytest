import pytest


@pytest.fixture(autouse=True, scope="class")
def setup():
    print('launch application')
    print('Open application browser')
    yield
    print("logout from application")
    print("close")
