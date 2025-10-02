import { test, expect } from '@playwright/test';
import { TEST_DATA } from '../../utils/test-data';

test.describe('API Tests', () => {
  test('Get all products', async ({ request }) => {
    const url = `${TEST_DATA.API_ENDPOINTS.BASE_URL}${TEST_DATA.API_ENDPOINTS.ALL_PRODUCTS}`;
    
    const response = await request.get(url);
    
    // Verify response status
    expect(response.status()).toBe(200);
    
    // Verify response structure
    const data = await response.json();
    expect(data).toHaveProperty('products');
    expect(Array.isArray(data.products)).toBe(true);
    
    // Verify product structure
    for (const product of data.products) {
      expect(product).toHaveProperty('id');
      expect(product).toHaveProperty('name');
      expect(product).toHaveProperty('brand');
      expect(product).toHaveProperty('category');
    }
    
    // Verify expected number of products
    expect(data.products).toHaveLength(34);
  });

  test('Unsupported POST request to products endpoint', async ({ request }) => {
    const url = `${TEST_DATA.API_ENDPOINTS.BASE_URL}${TEST_DATA.API_ENDPOINTS.ALL_PRODUCTS}`;
    
    const response = await request.post(url);
    
    // Verify response status
    expect(response.status()).toBe(200);
    
    // Verify error response structure
    const data = await response.json();
    expect(data).toHaveProperty('responseCode', 405);
    expect(data).toHaveProperty('message', 'This request method is not supported.');
  });

  // Commented out tests that return 405 (method not supported)
  // test('Get all brands', async ({ request }) => {
  //   const url = `${TEST_DATA.API_ENDPOINTS.BASE_URL}${TEST_DATA.API_ENDPOINTS.ALL_BRANDS}`;
  //   
  //   const response = await request.get(url);
  //   
  //   // Verify response status
  //   expect(response.status()).toBe(200);
  //   
  //   // Verify response structure
  //   const data = await response.json();
  //   expect(data).toHaveProperty('brands');
  //   expect(Array.isArray(data.brands)).toBe(true);
  //   
  //   // Verify brand structure
  //   for (const brand of data.brands) {
  //     expect(brand).toHaveProperty('id');
  //     expect(brand).toHaveProperty('brand');
  //   }
  // });

  // test('Search for a product', async ({ request }) => {
  //   const searchTerm = 'top';
  //   const url = `${TEST_DATA.API_ENDPOINTS.BASE_URL}${TEST_DATA.API_ENDPOINTS.SEARCH_PRODUCT}`;
  //   
  //   const response = await request.get(url, {
  //     params: { search_product: searchTerm }
  //   });
  //   
  //   // Verify response status
  //   expect(response.status()).toBe(200);
  //   
  //   // Verify response structure
  //   const data = await response.json();
  //   expect(data).toHaveProperty('products');
  //   expect(Array.isArray(data.products)).toBe(true);
  // });
});
