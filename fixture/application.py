from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixture.login_page import LoginPage



class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.wd.implicitly_wait(20)
        self.login = LoginPage(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()
