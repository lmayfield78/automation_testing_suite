import { test, expect } from '@playwright/test';
import { LoginPage } from '../../pages/LoginPage';
import { ProductsPage } from '../../pages/ProductsPage';
import { CheckoutPage } from '../../pages/CheckoutPage';
import { TEST_DATA } from '../../utils/test-data';

test.describe('E-commerce E2E Tests', () => {
  let loginPage: LoginPage;
  let productsPage: ProductsPage;
  let checkoutPage: CheckoutPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    productsPage = new ProductsPage(page);
    checkoutPage = new CheckoutPage(page);
    
    await loginPage.goto();
  });

  test('Complete e-commerce happy path flow', async ({ page }) => {
    // Login
    await loginPage.login();
    
    // Verify we're on the products page
    await expect(productsPage.title).toBeVisible();
    await expect(productsPage.title).toHaveText('Swag Labs');

    // Add products to cart
    await productsPage.addProductToCart(TEST_DATA.PRODUCTS.BACKPACK);
    await productsPage.addProductToCart(TEST_DATA.PRODUCTS.BIKE_LIGHT);
    await productsPage.addProductToCart(TEST_DATA.PRODUCTS.BOLT_TSHIRT);
    await productsPage.addProductToCart(TEST_DATA.PRODUCTS.FLEECE_JACKET);

    // Verify cart has items
    const cartCount = await productsPage.getCartItemCount();
    expect(cartCount).toBe(4);

    // Navigate to cart
    await productsPage.navigateToCart();

    // Start checkout
    await checkoutPage.startCheckout();

    // Fill personal information
    await checkoutPage.fillPersonalInfo();

    // Continue checkout
    await checkoutPage.continueCheckout();

    // Finish checkout
    await checkoutPage.finishCheckout();

    // Verify checkout completion
    await expect(checkoutPage.completeHeader).toBeVisible();
    await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');

    // Return to products
    await checkoutPage.returnToProducts();

    // Verify we're back on products page
    await expect(productsPage.title).toBeVisible();
  });

  test('Login with invalid credentials', async ({ page }) => {
    await loginPage.login(
      TEST_DATA.CREDENTIALS.INVALID_USER.username,
      TEST_DATA.CREDENTIALS.INVALID_USER.password
    );

    // Verify error message appears
    await expect(loginPage.errorMessage).toBeVisible();
    const errorText = await loginPage.getErrorMessage();
    expect(errorText).toContain('Username and password do not match');
  });

  test('Login with locked out user', async ({ page }) => {
    await loginPage.login(
      TEST_DATA.CREDENTIALS.LOCKED_USER.username,
      TEST_DATA.CREDENTIALS.LOCKED_USER.password
    );

    // Verify error message appears
    await expect(loginPage.errorMessage).toBeVisible();
    const errorText = await loginPage.getErrorMessage();
    expect(errorText).toContain('Sorry, this user has been locked out');
  });
});
