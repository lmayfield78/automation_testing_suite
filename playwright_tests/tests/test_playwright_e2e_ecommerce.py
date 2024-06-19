import pytest
from playwright.sync_api import Page
from pages.ecommerce_store import LoginPage, ProductsPage, CheckoutPage

pytestmark = pytest.mark.playwright

class TestPlaywrightEndToEndEcommerce:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        page.goto("https://www.saucedemo.com/")
        self.login_page = LoginPage(page)
        self.products_page = ProductsPage(page)
        self.checkout_page = CheckoutPage(page)

    def test_playwright_store_happy_path(self, page: Page):
        """ 
        This test will verify the very basic end to end happy path testing.
        From login to selection to checkout done in Selenium
        """
        self.login_page.login("standard_user", "secret_sauce")# enter username and password and click login
        self.products_page.add_product_to_cart("sauce-labs-backpack") # select items in the store - 1
        self.products_page.add_product_to_cart("sauce-labs-bolt-t-shirt") # select items in the store - 2
        self.products_page.add_product_to_cart("sauce-labs-bike-light") # select items in the store - 3
        self.products_page.add_product_to_cart("sauce-labs-fleece-jacket") # select items in the store - 4
        self.products_page.navigate_to_cart()
        self.checkout_page.checkout()
        self.checkout_page.fill_personal_info("John", "Doe", "12345") # enter personal info 
        self.checkout_page.continue_checkout()
        self.checkout_page.finish_checkout() 
        self.checkout_page.return_to_products() # click back to return to main store
