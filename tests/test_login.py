from common.common import NETTING_ACCOUNT


class TestLogin:
    def test_login(self, app):
        app.login.open()
        app.login.auth(NETTING_ACCOUNT.login, NETTING_ACCOUNT.password)
        assert app.login.total_field(), "Authorization failed"
