from locators.Login_page import Authorization


class LoginPage:
    def __init__(self, app):
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url)

    def auth_terminal(self, login, password, mt5_platform=True):
        if mt5_platform:
            self.select_mt5_platform().click()
        self.password_input().send_keys(password)
        self.login_input().send_keys(login)
        self.button_login().click()

    def password_input(self):
        return self.app.wd.find_element(*Authorization.PASSWORD_INPUT)

    def login_input(self):
        return self.app.wd.find_element(*Authorization.LOGIN_INPUT)

    def select_mt5_platform(self):
        return self.app.wd.find_element(*Authorization.MT5_PLATFORM)

    def button_login(self):
        return self.app.wd.find_element(*Authorization.BTN_LOGIN)

    def total_field(self):
        return self.app.wd.find_element(*Authorization.TOTAL_FIELD)
