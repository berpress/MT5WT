from fixture.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.login = LoginPage(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()
