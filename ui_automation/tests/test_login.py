# ui_automation/tests/test_login.py
from ui_automation.pages.login_page import LoginPage

def test_successful_login(browser):
    page = LoginPage(browser)
    page.load()
    page.enter_username("tomsmith")
    page.enter_password("SuperSecretPassword!")
    page.submit()

    # לאחר כניסה נכונה, צריך להופיע הטקסט "Secure Area"
    assert "Secure Area" in browser.page_source
