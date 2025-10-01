import pytest
from utils.browser_utils import Browser

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome or firefox")

@pytest.fixture(scope="session")
def browser(request):
    browser_type = request.config.getoption("--browser")
    # Handle case where browser_type might be a list
    if isinstance(browser_type, list):
        browser_type = browser_type[0] if browser_type else 'chrome'
    browser_instance = Browser(browser_type)
    browser_instance.start_browser()
    yield browser_instance
    browser_instance.driver.quit()