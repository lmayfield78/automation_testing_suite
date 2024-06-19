import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_utils import Browser



class EcommerceStore:

    string_assets = {
        "username": "standard_user",
        "password": "secret_sauce",
    }

    product_ids = {
        "backpack_id": "add-to-cart-sauce-labs-backpack",
        "bike_light_id": "add-to-cart-sauce-labs-bike-light",
        "bolt_shirt_id": "add-to-cart-sauce-labs-bolt-t-shirt",
        "fleece_jacket_id": "add-to-cart-sauce-labs-fleece-jacket",
        "onesie_id": "add-to-cart-sauce-labs-onesie",
        "onesie_tshirt_red_id": "add-to-cart-test.allthethings()-t-shirt-(red)",
    }

    def __init__(self, driver):
        self.driver = driver
        self.browser = Browser()
        self._username_field = (By.ID, "user-name")
        self._password_field = (By.ID, "password")
        self._login_button = (By.ID, "login-button")
        self._login_title = (By.CLASS_NAME, "login_logo")
        self._store_title = (By.CLASS_NAME, "app_logo")
        self._shopping_cart = (By.ID, "shopping_cart_container")
        self._checkout = (By.ID, "checkout")
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._zipcode = (By.ID, "postal-code")
        self._checkout_continue = (By.ID, "continue")
        self._checkout_finish = (By.ID, "finish")
        self._checkout_complete = (By.ID, "checkout_complete_container")

    @property
    def username_field(self):
        return self.driver.find_element(*self._username_field)  

    @property
    def password_field(self):
        return self.driver.find_element(*self._password_field)  


    @property
    def login_button(self):
        return self.driver.find_element(*self._login_button)  

    @property
    def login_title(self):
        return self.driver.find_element(*self._login_title)  

    @property
    def store_title(self):
        return self.driver.find_element(*self._store_title)
    
    @property
    def shopping_cart(self):
        return self.driver.find_element(*self._shopping_cart)
    
    @property
    def checkout(self):
        return self.driver.find_element(*self._checkout)

    @property
    def first_name(self):
        return self.driver.find_element(*self._first_name)
    
    @property
    def last_name(self):
        return self.driver.find_element(*self._last_name)
    
    @property
    def zipcode(self):
        return self.driver.find_element(*self._zipcode)
    
    @property
    def checkout_continue(self):
        return self.driver.find_element(*self._checkout_continue)
    
    @property
    def checkout_finish(self):
        return self.driver.find_element(*self._checkout_finish)
    
    @property
    def checkout_complete(self):
        return self.driver.find_element(*self._checkout_complete)
    

    def login(self, username, password, browser):
        # Wait until the username field is visible and interactable
        username_input = browser.wait_until_is_visible(self._username_field)  # Use the locator tuple directly
        username_input.send_keys(username)

        # Wait until the password field is visible and interactable
        password_input = browser.wait_until_is_visible(self._password_field)  # Use the locator tuple directly
        password_input.send_keys(password)

        # Wait until the submit button is clickable
        submit_btn = browser.wait_until_is_clickable(self._login_button)  # Use the locator tuple directly
        submit_btn.click()


    def select_random_products(self, count=3):
        # Selects 'count' unique product IDs at random from the product_ids dictionary
        selected_keys = random.sample(list(self.product_ids.keys()), count)
        # Fetch the WebElement for each selected product ID
        return [self.driver.find_element(By.ID, self.product_ids[key]) for key in selected_keys]
    