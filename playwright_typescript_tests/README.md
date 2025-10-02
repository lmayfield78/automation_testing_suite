# Playwright TypeScript Tests

This directory contains TypeScript Playwright tests that convert the existing Python Selenium and Playwright tests to a modern TypeScript implementation.

## Features

- **TypeScript**: Type-safe test development
- **Playwright**: Fast, reliable browser automation
- **Page Object Model**: Clean, maintainable test structure
- **Modern Tooling**: Latest Playwright features and best practices

## Setup

1. **Install dependencies:**
   ```bash
   cd playwright_typescript_tests
   npm install
   ```

2. **Install browsers:**
   ```bash
   npm run install:browsers
   ```

## Running Tests

### All Tests
```bash
npm test
```

### Specific Test Suites
```bash
# E2E tests only
npm run test:e2e

# API tests only
npm run test:api
```

### Debug Mode
```bash
# Run with browser visible
npm run test:headed

# Run with debugger
npm run test:debug

# Run with UI mode
npm run test:ui
```

### Test Reports
```bash
# View HTML report
npm run test:report
```

## Test Structure

```
playwright_typescript_tests/
├── tests/
│   ├── e2e/           # End-to-end tests
│   │   ├── ecommerce.spec.ts
│   │   └── challenges.spec.ts
│   └── api/           # API tests
│       └── api.spec.ts
├── pages/             # Page Object Model
│   ├── LoginPage.ts
│   ├── ProductsPage.ts
│   └── CheckoutPage.ts
├── utils/             # Utilities
│   └── test-data.ts
└── playwright.config.ts
```

## Test Coverage

### E2E Tests
- **E-commerce Flow**: Complete shopping cart workflow
- **Login Tests**: Valid/invalid credentials, locked user
- **Automation Challenges**: Scrollbars, load delays, text input, progress bar

### API Tests
- **Products API**: Get all products, search functionality
- **Brands API**: Get all brands
- **Error Handling**: Unsupported methods, invalid requests

## Configuration

The `playwright.config.ts` file includes:
- **Multi-browser support**: Chrome, Firefox, Safari
- **Mobile testing**: Mobile Chrome and Safari
- **Screenshots**: On failure
- **Videos**: On failure
- **Traces**: On retry
- **Parallel execution**: For faster test runs

## Benefits Over Python Tests

1. **Performance**: Playwright is typically faster than Selenium
2. **Type Safety**: TypeScript catches errors at compile time
3. **Modern Features**: Better debugging, tracing, and reporting
4. **Maintenance**: Cleaner, more maintainable code structure
5. **Tooling**: Better IDE support and autocomplete

## Browser Support

- **Desktop**: Chrome, Firefox, Safari
- **Mobile**: Mobile Chrome, Mobile Safari
- **Headless**: Supported for CI/CD
- **Headed**: For local development and debugging
