install-dependencies:
    pip install -r requirements.txt

run-selenium-tests:
    pytest selenium/tests

run-playwright-tests:
    pytest playwright/tests

run-api-tests:
    pytest api/tests

run-all-tests: run-selenium-tests run-playwright-tests run-api-tests

