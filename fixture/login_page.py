class LoginPage:
    def __init__(self, app):
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url)

    def authorization(self, login, password):
        pass
