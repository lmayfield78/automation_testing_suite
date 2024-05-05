import pytest
from .pages.LoginPage import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.browser.open("https://practicetestautomation.com/practice-test-login/")

    def test_login(self, browser):
        """ """

        # Create an instance of the LoginPage class
        log = LoginPage(browser.driver)

        # Call the login method of the LoginPage class
        log.login(log.string_assets["username"], log.string_assets["password"], browser)

        # Assert user is taken to success page
        assert (
            log.success.text == "Logged In Successfully"
        ), "Title should be 'Logged In Successfully'"

        # Logout
        log.logout.click()

        # Assert user is taken back to login page and contains the title "Test login" in the text
        assert (
            "Test login" in log.login_title_element.text
        ), "Title should contain 'Test login'"

    def test_login_invalid_password(self, browser):
        """ """

        # Create an instance of the LoginPage class
        log = LoginPage(browser.driver)

        # Call the login method of the LoginPage class
        log.login(log.string_assets["username"], "h23lj4h23lk4h23lj", browser)

        assert (
            browser.wait_until_is_visible(log.invalid_input).text
            == "Your password is invalid!"
        ), "Error message should be 'Your password is invalid!'"

    def test_invalid_username(self, browser):
        """ """

        # Create an instance of the LoginPage class
        log = LoginPage(browser.driver)

        # Call the login method of the LoginPage class
        log.login("MRChickenHead", log.string_assets["password"], browser)

        assert (
            browser.wait_until_is_visible(log.invalid_input).text
            == "Your username is invalid!"
        ), "Error message should be 'Your username is invalid!'"
