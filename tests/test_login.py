import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect
@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.enter_username("UFFPS1042A")
    login_page.wait_for_captcha()
    login_page.next_button()
    login_page.login_with_password()
    login_page.enter_password("password")
    login_page.click_login_button()
    #expect(page.get_by_role("textbox",name="Username")).to_be_visible()
    expect(page.locator(".navbar-brand h6")).to_be_visible(timeout=15000)
    '''page.title() == "Single Window System"
    expect(page).to_have_title("Single Window System", timeout=15000)'''

#@pytest.mark.regression
@pytest.mark.parametrize("username,expected_result",
                         [("UFFP","User not found."),
                          ("UFFPS104222","User not found."),
                          ("12345@","User not found."),
                          ("!@#$%^&*()","User not found.")])
def test_invalid_username(page,username,expected_result):
    login_page=LoginPage(page)
    login_page.open_login_page()
    login_page.enter_username(username)
    login_page.wait_for_captcha()
    login_page.next_button()
    expect(page.get_by_text(expected_result)).to_be_visible()

def test_blank_username(page):
    login_page=LoginPage(page)
    login_page.open_login_page()
    login_page.wait_for_captcha()
    login_page.next_button()
    expect(page.get_by_text("User Name cannot be left blank.")).to_be_visible()

@pytest.mark.parametrize("username,password,expected_result",
                         [("UFFPS1042A","passwordddd","Incorrect password. Please try again."),
                          ("EBCPM2146A","1234565","Incorrect password. Please try again."),
                          ("TQMPS0550J","wordpass","Incorrect password. Please try again."),
                          ("VKIUR7658N","qwerty","Incorrect password. Please try again.")])

def test_invalid_password(page,username,password,expected_result):
    login_page=LoginPage(page)
    login_page.open_login_page()
    login_page.enter_username(username)
    login_page.wait_for_captcha()
    login_page.next_button()
    login_page.login_with_password()
    login_page.enter_password(password)
    login_page.click_login_button()
    expect(page.get_by_text(expected_result)).to_be_visible()

    

    
