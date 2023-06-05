from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage


class HomePage:
    LOGIN_BUTTON_ID = "nav-link-accountList-nav-line-1"

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.ID, self.LOGIN_BUTTON_ID).click()
        return LoginPage(self.driver)
