

def test_basics(browser):
    browser.visit("https://www.google.com")
    assert browser.title == "Google"

