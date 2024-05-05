from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    def __init__(self, browser_type='chrome'):
        self.driver = None
        self.browser_type = browser_type

    def start_browser(self):
        if self.browser_type.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser_type.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser type")

    def open(self, url):
        self.driver.get(url)

    def wait_until_is_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not visible after {timeout} seconds.")
            return None

    def wait_until_is_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
