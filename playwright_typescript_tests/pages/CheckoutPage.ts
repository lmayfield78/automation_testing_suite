import { Page, Locator } from '@playwright/test';
import { TEST_DATA } from '../utils/test-data';

export class CheckoutPage {
  readonly page: Page;
  readonly checkoutButton: Locator;
  readonly firstNameInput: Locator;
  readonly lastNameInput: Locator;
  readonly postalCodeInput: Locator;
  readonly continueButton: Locator;
  readonly finishButton: Locator;
  readonly backToProductsButton: Locator;
  readonly completeHeader: Locator;

  constructor(page: Page) {
    this.page = page;
    this.checkoutButton = page.locator('[data-test="checkout"]');
    this.firstNameInput = page.locator('[data-test="firstName"]');
    this.lastNameInput = page.locator('[data-test="lastName"]');
    this.postalCodeInput = page.locator('[data-test="postalCode"]');
    this.continueButton = page.locator('[data-test="continue"]');
    this.finishButton = page.locator('[data-test="finish"]');
    this.backToProductsButton = page.locator('[data-test="back-to-products"]');
    this.completeHeader = page.locator('.complete-header');
  }

  async startCheckout(): Promise<void> {
    await this.checkoutButton.click();
  }

  async fillPersonalInfo(
    firstName: string = TEST_DATA.PERSONAL_INFO.FIRST_NAME,
    lastName: string = TEST_DATA.PERSONAL_INFO.LAST_NAME,
    postalCode: string = TEST_DATA.PERSONAL_INFO.POSTAL_CODE
  ): Promise<void> {
    await this.firstNameInput.fill(firstName);
    await this.lastNameInput.fill(lastName);
    await this.postalCodeInput.fill(postalCode);
  }

  async continueCheckout(): Promise<void> {
    await this.continueButton.click();
  }

  async finishCheckout(): Promise<void> {
    await this.finishButton.click();
  }

  async returnToProducts(): Promise<void> {
    await this.backToProductsButton.click();
  }

  async getCompleteMessage(): Promise<string> {
    return await this.completeHeader.textContent() || '';
  }

  async isCheckoutComplete(): Promise<boolean> {
    return await this.completeHeader.isVisible();
  }
}
