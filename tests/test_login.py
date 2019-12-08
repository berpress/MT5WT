from common.common import NETTING_ACCOUNT


class TestLogin:
    def test_login(self, app):
        app.auth.open()
        app.auth.auth_terminal(NETTING_ACCOUNT.login, NETTING_ACCOUNT.password)
        assert app.auth.total_field(), "Authorization failed"
