import pytest


@pytest.fixture()
def setup():
    print('launch application')
    print('Open application browser')
    yield
    print("logout from application")
    print("close")
