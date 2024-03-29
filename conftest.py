import pytest
from common.common import NETTING_ACCOUNT
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base_url")
    fixture = Application(base_url)
    fixture.wd.maximize_window()
    fixture.wd.implicitly_wait(10)
    yield fixture
    fixture.destroy()


def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        action="store",
        default="https://trade.mql5.com/trade",
        help="base_url",
    )


@pytest.fixture()
def auth_netting(app):
    if not app.auth.is_auth(NETTING_ACCOUNT.login):
        app.auth.open()
        app.auth.auth_terminal(NETTING_ACCOUNT.login, NETTING_ACCOUNT.password)
