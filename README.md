# QA Automation Testing Suite

A comprehensive automation testing framework showcasing multiple technologies and approaches for web and API testing. This suite demonstrates proficiency in both Python and TypeScript ecosystems, covering Selenium, Playwright, and API testing with modern best practices.

## tl;dr

```bash
# Clone and setup
git clone <repository-url>
cd automation_testing_suite

# Install dependencies (requires 'make' - macOS: usually pre-installed, Linux: apt install make, Windows: choco install make)
make install-all-dependencies

# Run everything
make run-all-tests-including-typescript

# Expect: Browser windows opening, tests running, results displayed
# Observe: E-commerce flows, API calls, automation challenges across 4 different frameworks
```

**No make?** See [Running Tests](#-running-tests) section for manual commands.

## 🚀 Quick Start

**Prerequisites:** Python 3.11+ and Node.js 18+

### Installing Prerequisites

**On macOS:**
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11+
brew install python@3.11

# Install Node.js
brew install node
```

**On Ubuntu/Debian:**
```bash
# Install Python 3.11+
sudo apt update
sudo apt install python3.11 python3.11-pip

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**On Windows:**
- Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
- Download Node.js 18+ from [nodejs.org](https://nodejs.org/)

### Running the Tests

```bash
# Clone the repository
git clone <repository-url>
cd automation_testing_suite

# Install all dependencies (Python + TypeScript)
make install-all-dependencies

# Run all tests (Python only)
make run-all-tests

# Run all tests including TypeScript
make run-all-tests-including-typescript
```

## 📁 Project Structure

This suite contains four distinct testing approaches, each demonstrating different technologies and methodologies:

### `selenium_tests/` - Python Selenium Framework
- **Technology:** Python + Selenium WebDriver + Pytest
- **Architecture:** Page Object Model with custom browser utilities
- **Features:** Explicit waits, no hard sleeps, maintainable locators
- **Tests:** E-commerce flow, login validation, cross-browser compatibility

### `playwright_tests/` - Python Playwright Framework  
- **Technology:** Python + Playwright + Pytest
- **Architecture:** Lightweight page objects, built-in assertions
- **Features:** Auto-waiting, challenge-based testing scenarios
- **Tests:** E-commerce flow, automation challenges (scrollbars, load delays, progress bars)

### `api_tests/` - Python API Testing
- **Technology:** Python + Requests + Pytest
- **Architecture:** Centralized constants, RESTful API validation
- **Features:** Status code validation, response structure verification
- **Tests:** Product endpoints, error handling, method validation

### `playwright_typescript_tests/` - Modern TypeScript Framework
- **Technology:** TypeScript + Playwright + Node.js
- **Architecture:** Type-safe page objects, modern tooling
- **Features:** Multi-browser support, screenshots/videos on failure, debugging tools
- **Tests:** Complete e-commerce suite, API testing, automation challenges

## 🛠️ Running Tests

### Python Tests (Selenium, Playwright, API)
```bash
# Install Python dependencies
make install-dependencies

# Run individual test suites
make run-selenium-tests      # Selenium WebDriver tests
make run-playwright-tests    # Python Playwright tests  
make run-api-tests          # API tests

# Run all Python tests
make run-all-tests
```

### TypeScript Tests
```bash
# Install TypeScript dependencies
make install-typescript-dependencies

# Run TypeScript tests
make run-typescript-tests

# Or run individual TypeScript test suites
cd playwright_typescript_tests
npm run test:e2e           # E2E tests only
npm run test:api           # API tests only
npm run test:headed        # With browser visible
npm run test:debug         # Debug mode
```

### All Tests (Python + TypeScript)
```bash
# Install all dependencies
make install-all-dependencies

# Run all tests
make run-all-tests-including-typescript
```

## 🎯 Key Strengths

### **Multi-Language Proficiency**
- **Python:** Demonstrates expertise in the most popular automation language
- **TypeScript:** Shows modern web development skills and type safety
- **Both:** Proves adaptability across different tech stacks

### **Framework Diversity**
- **Selenium:** Industry standard, shows deep understanding of WebDriver
- **Playwright:** Modern alternative, demonstrates keeping up with trends
- **API Testing:** Essential for full-stack testing capabilities

### **Best Practices Implementation**
- **Page Object Model:** Maintainable, scalable test architecture
- **Explicit Waits:** Reliable test execution without flakiness
- **Type Safety:** Compile-time error detection in TypeScript
- **CI/CD Ready:** GitHub Actions integration for continuous testing

### **Real-World Scenarios**
- **E-commerce Testing:** Complete user journey validation
- **Challenge Testing:** Common automation problems (timing, dynamic content)
- **API Validation:** RESTful service testing with error handling
- **Cross-Browser:** Multi-browser compatibility verification

## 🔧 Technical Highlights

### **Selenium Implementation**
- Custom browser utilities with proper driver management
- Chrome options to handle password manager popups
- Session-scoped fixtures for efficient test execution
- No hard sleeps - explicit waits throughout

### **Playwright Features**
- Built-in auto-waiting and retry mechanisms
- Screenshot and video capture on failures
- Trace viewer for debugging complex issues
- Multi-browser project configuration

### **TypeScript Advantages**
- Compile-time error detection
- Better IDE support and autocomplete
- Modern async/await patterns
- Type-safe page object implementations

## 🚦 CI/CD Integration

The suite includes GitHub Actions workflows for:
- **Merge Testing:** Runs on every pull request to main
- **Nightly Testing:** Scheduled runs Monday-Friday at 1 AM
- **Multi-Browser:** Tests across Chrome, Firefox, and Safari
- **Artifact Collection:** Screenshots, videos, and traces on failures

## 📊 Test Coverage

- **E-commerce Flows:** Login, product selection, checkout, order completion
- **Authentication:** Valid/invalid credentials, locked user scenarios  
- **API Endpoints:** GET/POST methods, error handling, response validation
- **UI Challenges:** Dynamic content, timing issues, element interactions
- **Cross-Browser:** Chrome, Firefox, Safari compatibility

This suite demonstrates a comprehensive understanding of modern QA automation, from traditional Selenium approaches to cutting-edge TypeScript implementations, providing a solid foundation for any automation testing role.
