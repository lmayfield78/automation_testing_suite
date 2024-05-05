from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_utils import Browser


class LoginPage:

    string_assets = {
        "username": "student",
        "password": "Password123",
    }

    def __init__(self, driver):
        self.driver = driver
        self.browser = Browser()
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
        self.login_title = (By.ID, "login")
        self.success_title = (By.CSS_SELECTOR, "h1.post-title")
        self.logout_button = (By.XPATH, "//a[contains(@class, 'wp-block-button__link')]")
        self.invalid_input = (By.XPATH, "//*[@id='error' and contains(@class, 'show')]")
        self.invalid_password_message = (By.CSS_SELECTOR, "p.login-error")


    @property
    def username(self):
        return self.driver.find_element(*self.username_field)  

    @property
    def password(self):
        return self.driver.find_element(*self.password_field)  

    @property
    def submit(self):
        return self.driver.find_element(*self.submit_button)  

    @property
    def login_title_element(self):
        return self.driver.find_element(*self.login_title)  

    @property
    def success(self):
        return self.driver.find_element(*self.success_title)  

    @property
    def logout(self):
        return self.driver.find_element(*self.logout_button)
    
    @property
    def invalid(self):
        return self.driver.find_element(*self.invalid_input)

    def login(self, username, password, browser):
        # Wait until the username field is visible and interactable
        username_input = browser.wait_until_is_visible(self.username_field)
        username_input.send_keys(username)

        # Wait until the password field is visible and interactable
        password_input = browser.wait_until_is_visible(self.password_field)
        password_input.send_keys(password)

        # Wait until the submit button is clickable
        submit_btn = browser.wait_until_is_clickable(self.submit_button)
        submit_btn.click()
