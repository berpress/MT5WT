import pytest
from fixture.application import Application


@pytest.fixture()
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()
