from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.wd.implicitly_wait(4)

    def destroy(self):
        self.wd.quit()
