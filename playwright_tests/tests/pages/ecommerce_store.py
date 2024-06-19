from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = self.page.locator('[data-test="username"]')
        self.password_input = self.page.locator('[data-test="password"]')
        self.login_button = self.page.locator('[data-test="login-button"]')

    def login(self, username: str, password: str):
        self.username_input.click()
        self.username_input.fill(username)
        self.password_input.click()
        self.password_input.fill(password)
        self.login_button.click()


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def add_product_to_cart(self, product_id: str):
        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def navigate_to_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = self.page.locator('[data-test="firstName"]')
        self.last_name_input = self.page.locator('[data-test="lastName"]')
        self.postal_code_input = self.page.locator('[data-test="postalCode"]')
        self.checkout_button = self.page.locator('[data-test="checkout"]')
        self.continue_button = self.page.locator('[data-test="continue"]')
        self.finish_button = self.page.locator('[data-test="finish"]')
        self.back_to_products_button = self.page.locator('[data-test="back-to-products"]')

    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.wait_for_selector("[data-test='firstName']", state="attached")
        self.first_name_input.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.click()
        self.last_name_input.fill(last_name)
        self.postal_code_input.click()
        self.postal_code_input.fill(postal_code)

    def checkout(self):
        self.checkout_button.click()

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def return_to_products(self):
        self.back_to_products_button.click()