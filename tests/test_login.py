from common.common import NETTING_ACCOUNT

import logging

file_log = logging.FileHandler("Log.log")
console_out = logging.StreamHandler()

logging.basicConfig(
    handlers=(file_log, console_out),
    format="[%(asctime)s | %(levelname)s]: %(message)s",
    datefmt="%m.%d.%Y %H:%M:%S",
    level=logging.INFO,
)

logging.info("Info message??))")


class TestLogin:
    def test_login(self, app):
        app.auth.open()
        app.auth.auth_terminal(NETTING_ACCOUNT.login, NETTING_ACCOUNT.password)
        assert app.auth.total_field(), "Authorization failed"
