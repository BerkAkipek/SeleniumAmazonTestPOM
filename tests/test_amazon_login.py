from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestAmazonLogin(BaseClass):

    def test_amazon_login(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_login()
        login_page.fill_email()
        login_page.fill_password()
        login_page.assert_failure()
