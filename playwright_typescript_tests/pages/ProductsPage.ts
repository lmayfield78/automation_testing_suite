import { Page, Locator } from '@playwright/test';
import { TEST_DATA } from '../utils/test-data';

export class ProductsPage {
  readonly page: Page;
  readonly title: Locator;
  readonly shoppingCartLink: Locator;
  readonly cartBadge: Locator;

  constructor(page: Page) {
    this.page = page;
    this.title = page.locator('.app_logo');
    this.shoppingCartLink = page.locator('[data-test="shopping-cart-link"]');
    this.cartBadge = page.locator('.shopping_cart_badge');
  }

  async addProductToCart(productId: string): Promise<void> {
    const addToCartButton = this.page.locator(`[data-test="add-to-cart-${productId}"]`);
    await addToCartButton.click();
  }

  async removeProductFromCart(productId: string): Promise<void> {
    const removeButton = this.page.locator(`[data-test="remove-${productId}"]`);
    await removeButton.click();
  }

  async navigateToCart(): Promise<void> {
    await this.shoppingCartLink.click();
  }

  async getCartItemCount(): Promise<number> {
    const badgeText = await this.cartBadge.textContent();
    return badgeText ? parseInt(badgeText) : 0;
  }

  async isProductInCart(productId: string): Promise<boolean> {
    const removeButton = this.page.locator(`[data-test="remove-${productId}"]`);
    return await removeButton.isVisible();
  }

  async getPageTitle(): Promise<string> {
    return await this.title.textContent() || '';
  }
}
