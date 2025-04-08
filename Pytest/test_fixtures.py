import pytest


@pytest.fixture()
def setup():
    print('launch application')
    print('Open application browser')
    yield
    print("logout from application")
    print("close")


def test_with_valid_credentails(setup):
    print("here we are entering valid crdentails")

def test_invlaid_credentials(setup):
    print("enterning invalid credentaisl")