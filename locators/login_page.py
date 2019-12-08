from selenium.webdriver.common.by import By


class Authorization:
    LOGIN_INPUT = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")
    SAVE_PASSWORD_CHECKBOX = (By.ID, "save")
    SERVER_INPUT = (By.ID, "server")
    MT4_PLATFORM = (By.ID, "mt4-platform")
    MT5_PLATFORM = (By.ID, "mt5-platform")
    BTN_LOGIN = (By.XPATH, "//button[@class='input-button' and  text()='OK']")
    TOTAL_FIELD = (By.ID, "total")
    ACCOUNT_INFO = (By.CLASS_NAME, "page-text account")
