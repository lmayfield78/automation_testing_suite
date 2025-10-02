// Test data constants
export const TEST_DATA = {
  // Login credentials
  CREDENTIALS: {
    VALID_USER: {
      username: 'standard_user',
      password: 'secret_sauce'
    },
    INVALID_USER: {
      username: 'invalid_user',
      password: 'invalid_password'
    },
    LOCKED_USER: {
      username: 'locked_out_user',
      password: 'secret_sauce'
    }
  },

  // Personal information for checkout
  PERSONAL_INFO: {
    FIRST_NAME: 'John',
    LAST_NAME: 'Doe',
    POSTAL_CODE: '12345'
  },

  // Product IDs
  PRODUCTS: {
    BACKPACK: 'sauce-labs-backpack',
    BIKE_LIGHT: 'sauce-labs-bike-light',
    BOLT_TSHIRT: 'sauce-labs-bolt-t-shirt',
    FLEECE_JACKET: 'sauce-labs-fleece-jacket',
    ONESIE: 'sauce-labs-onesie',
    RED_TSHIRT: 'test.allthethings()-t-shirt-(red)'
  },

  // API endpoints
  API_ENDPOINTS: {
    BASE_URL: 'https://automationexercise.com/',
    ALL_PRODUCTS: 'api/productsList',
    ALL_BRANDS: 'api/brandList',
    SEARCH_PRODUCT: 'api/searchProduct',
    LOGIN: 'api/verifyLogin/',
    UPDATE_ACCOUNT: 'api/updateAccount'
  }
} as const;
