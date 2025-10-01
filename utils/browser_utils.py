import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Browser:
    def __init__(self, browser_type='chrome'):
        self.driver = None
        self.browser_type = browser_type

    def start_browser(self):
        if self.browser_type.lower() == 'chrome':
            options = Options()
            
            # Check if HEADLESS environment variable is set
            if os.getenv('HEADLESS', '').lower() in ('true', '1', 'yes'):
                options.add_argument('--headless')  # Run in headless mode for CI
            
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            
            # Disable Chrome password manager and autofill
            options.add_argument('--disable-save-password-bubble')
            options.add_argument('--disable-autofill')
            options.add_argument('--disable-password-manager')
            options.add_argument('--disable-web-security')
            options.add_argument('--disable-features=VizDisplayCompositor')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-plugins')
            options.add_argument('--disable-images')
            options.add_argument('--disable-background-timer-throttling')
            options.add_argument('--disable-backgrounding-occluded-windows')
            options.add_argument('--disable-renderer-backgrounding')
            options.add_argument('--disable-features=TranslateUI')
            options.add_argument('--disable-ipc-flooding-protection')
            options.add_experimental_option('prefs', {
                'credentials_enable_service': False,
                'profile.password_manager_enabled': False,
                'profile.default_content_setting_values.notifications': 2,
                'profile.default_content_settings.popups': 0,
                'profile.managed_default_content_settings.images': 2,
                'profile.password_manager_leak_detection': False,
                'profile.default_content_setting_values.media_stream': 2,
                'profile.default_content_setting_values.geolocation': 2,
                'profile.default_content_setting_values.camera': 2,
                'profile.default_content_setting_values.microphone': 2
            })
            options.add_experimental_option('useAutomationExtension', False)
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            options.add_experimental_option('detach', True)
            
            # Use Service for better driver management
            service = Service()
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

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
