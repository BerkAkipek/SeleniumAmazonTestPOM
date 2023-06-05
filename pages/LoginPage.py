from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT_ID = "ap_email"
    EMAIL_SUBMIT_BUTTON_ID = "continue"
    PASSWORD_INPUT_ID = "ap_password"
    PASSWORD_SUBMIT_BUTTON_ID = "signInSubmit"
    FAIL_MASSAGE_XPATH = "//span[@class='a-list-item']"

    def __init__(self, driver):
        self.driver = driver

    def fill_email(self):
        self.driver.find_element(By.ID, self.EMAIL_INPUT_ID).send_keys("mail@mail.com")
        self.driver.find_element(By.ID, self.EMAIL_SUBMIT_BUTTON_ID).click()

    def fill_password(self):
        self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID).send_keys("P@22word")
        self.driver.find_element(By.ID, self.PASSWORD_SUBMIT_BUTTON_ID).click()

    def assert_failure(self):
        assert "Şifreniz yanlış" in self.driver.find_element(By.XPATH, self.FAIL_MASSAGE_XPATH).text
