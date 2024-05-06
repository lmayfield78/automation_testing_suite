import pytest
from playwright.sync_api import Page, expect


class TestChallenges:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        page.goto("http://uitestingplayground.com/")

    def test_hard_to_find_challenge(self, page: Page):
        """
        This test will find a hidden link. Sometimes elements are hidden
        and require users to scroll into view in order to access the element.
        The test consists of clicking on the Scrollbars, waiting for the Hiding Button to appear,
        and then clicking on the Hiding Button.
        """

        page.get_by_role("link", name="Scrollbars").click()
        expect(page.get_by_role("button", name="Hiding Button"))
        page.get_by_role("button", name="Hiding Button").click()

    def test_load_delay_challenge(self, page: Page):
        """
        This test is challenged with waiting for an element to load. It is common for there
        to be a delay when content is loading which forces the test to wait for the element to load.
        This test displays how easy playwright handles this challenge.
        """

        page.get_by_role("link", name="Load Delay").click()

        # Click on the button that appears after a delay (Built in wait & verifications)
        page.get_by_role("button", name="Button Appearing After Delay").click()

    def test_text_input_challenge(self, page: Page):
        """
        This verifies that when a user inputs text into the input field,
        the button's text changes to match the input value.
        Note! If you don't click on the input field the keys will not be registered
        and the button will not update. The test will fail. This differntiates the difference between
        a type of test that just attempts to enter text into the input field and a type of test
        that clicks on the input field and then enters text into the input field, more reflects an actual user.
        """
        b_text_1 = "Button That Should Change it's Name Based on Input Value"
        b_text_2 = "The button text has been changed"

        # go to text input challenge page
        page.get_by_role("link", name="Text Input").click()

        # store button value and assert button text matches value of 'b_text_1'
        button = page.get_by_role("button")
        expect(button).to_have_text(b_text_1)

        # click on input prior to inputing keys. IMPORTANT!!! If you don't click on the input
        # the keys will not be registered and the button will not update. The test will fail.
        page.get_by_placeholder("MyButton").click()

        # input text into input
        page.get_by_placeholder("MyButton").fill(b_text_2)

        # click on button
        page.get_by_role("button").click()

        # assert button text matches value of 'b_text_2'
        expect(button).to_have_text(b_text_2)

    def test_progress_bar_challenge(self, page: Page):
        """
        This test is challenged with continaully watching the progress bar
        and clicking on the stop button when it reaches 75% completion. The goal is to have a test that is
        capable of observing the progress of an event and knowing when to properly respond.
        If the test is slow(stopped above 75%)the result will be above 0.
        """

        # Go to progress bar challenge page
        page.get_by_role("link", name="Progress Bar").click()

        # Click on start button to begin status bar progression
        page.get_by_role("button", name="Start").click()

        # Wait until the progress bar reaches 75%
        page.wait_for_function(
            "document.querySelector('#progressBar').getAttribute('aria-valuenow') === '75'"
        )

        # Click on the stop button
        page.get_by_role("button", name="Stop").click()

        # Store the result text in a variable
        result_text = page.get_by_text("Result: 0, duration:").text_content()

        # Store the progress value
        progress_value = int(
            page.query_selector("#progressBar").get_attribute("aria-valuenow")
        )

        # Check if the progress value is 75% or above
        if progress_value == 75:
            assert (
                "Result: 0" in result_text
            ), f"Perfect stop at 75%, but got {result_text}"  # perfect test
        elif progress_value > 75:
            # Check if the result is above 0, indicating a slow test
            result_number = int(
                result_text.split(":")[1].strip().split(",")[0]
            )  # String manipulation to get the number
            if result_number > 0:
                assert (
                    True
                ), f"Test is slow, stopped at {progress_value}% with result {result_number}"  # slow test
            else:
                print(f"Test stopped at {progress_value}% with result: {result_text}")
        else:
            assert False, f"Test failed, stopped before 75% at {progress_value}%"
