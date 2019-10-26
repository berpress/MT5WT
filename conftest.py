import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base_url")
    fixture = Application(base_url)
    fixture.wd.maximize_window()
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", action="store", default="https://trade.mql5.com/trade", help="base_url"
    )
