from fixture.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Application:
    def __init__(self, base_url):
        options: Options = Options()
        options.headless = True
        driver = ChromeDriverManager().install()
        self.wd = webdriver.Chrome(driver, options=options)
        self.auth = LoginPage(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()
