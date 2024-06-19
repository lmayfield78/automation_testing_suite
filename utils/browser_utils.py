from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Ensure this is imported


class Browser:
    def __init__(self, browser_type='chrome'):
        self.driver = None
        self.browser_type = browser_type

    def start_browser(self):
        self.driver = webdriver.Chrome()

    def open(self, url):
        self.driver.get(url)

    def wait_until_is_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            # Ensure locator is a tuple, e.g., (By.ID, "element_id")
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            # Handle timeout exception or re-raise with a custom message
            raise TimeoutException(f"Element with locator {locator} not visible after {timeout} seconds")

    def wait_until_is_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
