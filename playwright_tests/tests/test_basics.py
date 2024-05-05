
# pytestmark = [pytest.mark.testlevel_integration]


# class TestTempTesting:
#     """
#     Temp placeholder tests
#     Using page objects. Soon to be deleted
#     """

# def test_x(self, page: Page):
#     page.goto("http://uitestingplayground.com/")
#     props = Props(page)
#     expect(props.title).to_be_visible()
#     # expect(props.title).to_be_hidden() # This is used to test github actions. Uncomment to verify failures.

# This is used to test github actions. Uncomment to verify failures.
# def test_x_2(self, page: Page):
#     page.goto("http://uitestingplayground.com/")
#     props = Props(page)
#     # expect(props.title).to_be_visible()
#     expect(props.title).to_be_hidden()

# This is used to test github actions. Uncomment to verify failures.
# @pytest.mark.xfail
# def test_fail_1(self):
#     assert 3 + 6 == 33

# This is used to test github actions. Uncomment to verify failures.
# def test_fail_2(self):
#     assert 66 + 8 == 33


from playwright.sync_api import Page


class Props:
    def __init__(self, page: Page):
        self.title = page.locator("#title")


from playwright.sync_api import Page, expect
import pytest

# pytestmark = [pytest.mark.testlevel_integration]


"""
The following are just test examples of how to use playwright.
 These tests will eventually be deleted. 

 Use the following templates to get an example of what can be done. 
(These examples were from the Playwright Demo)
"""


# http://uitestingplayground.com/
@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
def test_hard_to_find(page: Page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Scrollbars").click()
    expect(page.get_by_role("button", name="Hiding Button"))
    page.get_by_role("button", name="Hiding Button").click()

    # (1) --headed <- add this to the end of test run to add browsers
    # (2) --slowmo 600 <- add this flag to slow down the test if it goes too fast.


@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
def test_load_delay(page: Page):
    page.goto("http://uitestingplayground.com/")
    page.goto("http://uitestingplayground.com/loaddelay")
    page.get_by_role("button", name="Button Appearing After Delay").click()


# Works with all Browsers (Runs both Chrome And FireFox)
@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
def test_all_browsers(page: Page):
    page.goto("https://staging.posit.cloud/")
    page.get_by_role("link", name="Log In", exact=True).click()
    expect(page.get_by_text("Log In", exact=True))


# Only works with FireFox
@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
@pytest.mark.only_browser("firefox")
def test_firefox(page: Page):
    page.goto("https://staging.posit.cloud/")
    page.get_by_role("link", name="Log In", exact=True).click()
    expect(page.get_by_text("Log In", exact=True))


# Only works with Chrome
@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
@pytest.mark.only_browser("chromium")
def test_chrome(page: Page):
    page.goto("https://staging.posit.cloud/")
    page.get_by_role("link", name="Log In", exact=True).click()
    expect(page.get_by_text("Log In", exact=True))


@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
def test_codegen(page: Page):
    # Use command 'playwright codegen https://staging.posit.cloud/'
    page.goto("https://staging.posit.cloud/")
    # add steps here
    page.get_by_role("link", name="Get Started", exact=True).click()
    page.locator("td:nth-child(3) > .button").first.click()
    page.get_by_role("row", name="Concurrent Projects Unlimited").get_by_role("button").click()


@pytest.mark.skip(reason="This is a sample test. Soon to be deleted")
def test_helpful_debug(page: Page):
    page.goto("https://staging.posit.cloud/")
    page.goto(
        "https://login.staging.posit.cloud/login?redirect=%2Foauth%2Fauthorize%3Fredirect_uri%3Dhttps%253A%252F%252Fstaging.posit.cloud%252Flogin%26client_id%3Dposit-cloud-staging%26response_type%3Dcode%26show_auth%3D0"
    )
    page.get_by_placeholder("Email").fill("connect-qa+701@rstudio.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_placeholder("Password").fill("darbycarriesasword")
    page.get_by_role("button", name="Log In").click()
    # === The following examples below are examples of good and bad locators.
    # View the debugger to assist in some examples ===

    # Using this line of code will fail the test.
    # expect(page.get_by_text("Your Content")).to_be_visible(timeout=60_000)

    # Using these examples would pass the test. Examples of good locators.
    # expect(page.get_by_text("Your Content").nth(1)).to_be_visible(timeout=60_000)
    # expect(page.get_by_role("link", name="Your Content")).to_be_visible(timeout=60_000)

    # Helpers when running tests
    # (1) page.pause() <- This is similar to 'pdb.set_trace()' w/ import pdb; pdb.set_trace()
    # Also breakpoint() is also an option.

    # (2) PWDEBUG=1 pytest -s <- Use this function to run the test in debug mode. Similar to the --pdb flag

    # (3) --tracing on   // playwright show-trace (path)trace.zip
    #        // retain-on-failure  // trace.playwright.dev  // (yes video & screenshot)
    # (4) pytest.ini <-- pytest flags can be housed in this file.


