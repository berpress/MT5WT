
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, app):
        self.app = app

    def open(self):
        self.app.wd.get(self.app.base_url)
