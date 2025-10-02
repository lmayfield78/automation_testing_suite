import { test, expect } from '@playwright/test';

test.describe('Automation Challenges', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://uitestingplayground.com/');
  });

  test('Hard to find challenge - Scrollbars', async ({ page }) => {
    // Navigate to Scrollbars page
    await page.getByRole('link', { name: 'Scrollbars' }).click();

    // Wait for the hiding button to appear and click it
    const hidingButton = page.getByRole('button', { name: 'Hiding Button' });
    await expect(hidingButton).toBeVisible();
    await hidingButton.click();
  });

  test('Load delay challenge', async ({ page }) => {
    // Navigate to Load Delay page
    await page.getByRole('link', { name: 'Load Delay' }).click();

    // Click on the button that appears after a delay
    const delayedButton = page.getByRole('button', { name: 'Button Appearing After Delay' });
    await delayedButton.click();
  });

  test('Text input challenge', async ({ page }) => {
    const buttonText1 = "Button That Should Change it's Name Based on Input Value";
    const buttonText2 = "The button text has been changed";

    // Navigate to Text Input page
    await page.getByRole('link', { name: 'Text Input' }).click();

    // Get the button and verify initial text
    const button = page.getByRole('button');
    await expect(button).toHaveText(buttonText1);

    // Click on input field and enter new text
    const input = page.getByPlaceholder('MyButton');
    await input.click();
    await input.fill(buttonText2);

    // Click the button
    await button.click();

    // Verify button text has changed
    await expect(button).toHaveText(buttonText2);
  });

  test('Progress bar challenge', async ({ page }) => {
    // Navigate to Progress Bar page
    await page.getByRole('link', { name: 'Progress Bar' }).click();

    // Click start button
    await page.getByRole('button', { name: 'Start' }).click();

    // Wait until progress reaches 75%
    await page.waitForFunction(
      () => document.querySelector('#progressBar')?.getAttribute('aria-valuenow') === '75'
    );

    // Click stop button
    await page.getByRole('button', { name: 'Stop' }).click();

    // Get the result text
    const resultText = await page.getByText('Result: 0, duration:').textContent();
    
    // Get the progress value
    const progressValue = await page.locator('#progressBar').getAttribute('aria-valuenow');
    const progress = progressValue ? parseInt(progressValue) : 0;

    // Verify the result
    if (progress === 75) {
      expect(resultText).toContain('Result: 0');
    } else if (progress > 75) {
      // If stopped after 75%, the result should be > 0
      const resultNumber = resultText ? parseInt(resultText.split(':')[1].trim().split(',')[0]) : 0;
      expect(resultNumber).toBeGreaterThan(0);
    } else {
      throw new Error(`Test failed, stopped before 75% at ${progress}%`);
    }
  });
});
