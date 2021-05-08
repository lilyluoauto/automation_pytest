import pytest


@pytest.yield_fixture()
def setup():
    yield
    print("done")


def test_pass(setup):
    assert True


def test_fail(setup):
    assert False
