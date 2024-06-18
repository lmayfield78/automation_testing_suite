# QA Automation Framework

This project is a a QA automation suite that uses Selenium, Playwright and API's with Pytest to automate web and api content. 

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Automated Tests](#automated-tests)
    - [Selenium Tests](#selenium-tests)
    - [Playwright Tests](#playwright-tests)
    - [API Tests](#api-tests)
4. [Makefile Commands](#makefile-commands)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
The idea behind this project is to display a QA automation suite that can automate the testing of the website and Api's. The idea behind is less about covering a large scope of testing tests, but rather showcase a few tests that can be used as a starting point for a QA automation suite. There are three types of Automated tests that are included in this project. 1) Selenium Tests, 2) Playwright Tests, and 3) API Tests. They are all written in Python using Pytest as the test runner. For ease of use, a Makefile is provided to install dependencies, run each type of test individually or all tests at once.

## Setup
Once you have cloned the repo, you can install the dependencies using the Makefile command `make install-dependencies`. This will install the dependencies from the requirements.txt file.

## Automated Tests
The automated test sections below will include the details and the reasoning of why I chose to structure the tests in the way I did.

### Selenium Tests
The selenium tests are located in the `selenium_tests/tests` directory. It includes a `pages` directory for the page objects and a `tests` directory for the tests as well as `conftest.py` file that is used to facilitate the pytest runner. The utils directory houses a `browser_utils.py` file that is used to show the helper functions that are used to run the tests.

Note: I attempted to design the selenium tests in this way to showcase how the tests can be streamlined for better readability and maintainability. I don't use sleeps and I don't like using hard to read locators. I find Selenium's default options can be a bit cumbersome to work with and I prefer to keep the tests as readable as possible.

These tests can be run using the Makefile command `make run-selenium-tests`. (if you're not familiar with pytest)

### Playwright Tests
The playwright tests are located in the `playwright_tests/tests` directory. It does not includes `tests` directory for the tests as well as `conftest.py` file that is used to facilitate the pytest runner(nothing active in it now). There is no page object directory because the tests are so simple that they don't need it. I believe Playwright is a more efficient automation tool than its competitors because it has many of its assertion features built into each of its functions.

These tests are simple tests that I believe cover some of the challenges of automated testing. I chose of a few of the automation challenges that are common in the industry and wanted to display how easily playwright handles them. 

These tests can be run using the Makefile command `make run-playwright-tests`. (if you're not familiar with pytest)


### API Tests
The api tests are located in the `api_tests/tests` directory. It includes a `constants.py` file housing the test endpoints and a `test_api.py` file housing the tests as well as `conftest.py` file (not active) that is used to facilitate the pytest runner. These test are few and basic. The idea behind the tests is to showcase the use of the framework and the ability to test the api's.

These tests can be run using the Makefile command `make run-api-tests`. (if you're not familiar with pytest)

### CI / Github actions Runs
There are two continuious integration runs set up for this repository. 
1) When there is a merge into main
2) A nightly run that runs at 1 am Monday through Friday

## Makefile Commands
The Makefile is intended to allow anyone who wasn't familiar with pytest to run the tests. Anyone can run these commands without the headache of setting up the environment and having to deal with a variety of commands. Below is a list of the commands you can use to run the tests.

Makefile commands:
- `make install-dependencies`: Install dependencies from requirements.txt. (DO THIS FIRST!)
- `make run-selenium-tests`: Run Selenium tests.
- `make run-playwright-tests`: Run Playwright tests.
- `make run-api-tests`: Run API tests.
- `make run-all-tests`: Run all automated tests.
