from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from pages.HomePage import HomePage


def test_case():
    service_obj = Service("/home/berkakipek/WebDrivers/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.amazon.com.tr/")

    home_page = HomePage(driver)
    login_page = home_page.click_login()
    login_page.fill_email()
    login_page.fill_password()
    login_page.assert_failure()


def main():
    test_case()


if __name__ == '__main__':
    main()
