from common.common import NETTING_ACCOUNT
import pytest


class TestLogin:
    @pytest.mark.issue("#1")
    def test_login(self, app):
        app.login.open()
        app.login.auth(NETTING_ACCOUNT.login, NETTING_ACCOUNT.password)
        assert app.login.total_field(), "Authorization failed"
