import pytest
from selenium.webdriver.common.by import By
from .pages.ecommercePages import EcommerceStore

pytestmark = pytest.mark.selenium

class TestEndToEndEcommerce:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.browser.open("https://www.saucedemo.com/")

    def test_store_happy_path(self, browser):
        """ 
        This test will verify the very basic end to end happy path testing.
        From login to selection to checkout
        """

        # Create an instance of the LoginPage class
        store = EcommerceStore(browser.driver)

        # Call the login method of the LoginPage class
        store.login(store.string_assets["username"], store.string_assets["password"], browser)

        # Assert user is taken to shopping page
        assert (
            store.store_title.text == "Swag Labs"
        ), "Title should be 'Swag Labs'"

        # generate random product ids to select from store
        random_product_elements = store.select_random_products()

        # Add each selected product to the cart
        for product_element in random_product_elements:
            product_element.click()

        #click the cart button to go to cart page
        store.shopping_cart.click()

        # verify that checkout button is displayed
        # this also verifies that the user is on the correct screen
        self.browser.wait_until_is_clickable(store.checkout)
        store.checkout.click()

        # User is taken to personal verification page
        #fill out the personal info
        first_name_input = self.browser.wait_until_is_visible((By.ID, "first-name"))
        first_name_input.send_keys("John")

        last_name_input = self.browser.wait_until_is_visible((By.ID, "last-name"))
        last_name_input.send_keys("Doe")

        zipcode_input = self.browser.wait_until_is_visible((By.ID, "postal-code"))
        zipcode_input.send_keys("12345")

        # click the continue button
        store.checkout_continue.click()

        # click the finish checkout button
        store.checkout_finish.click()

            


    