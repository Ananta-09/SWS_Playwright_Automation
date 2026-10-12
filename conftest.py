import allure
import pytest
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
'''@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()'''
@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        browser_name= request.config.getoption("--browser")
        if browser_name == "chromium":
            browser=p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser=p.firefox.launch(headless=False)
        elif browser_name == "edge":
            browser = p.chromium.launch(channel="msedge", headless=False)
        '''else:
            raise ValueError("Enter a valid browser: chromium, firefox, or edge")''' #as i have mentioned in the pytest_addoption function, the choices are already defined, so this else block is not necessary. If an invalid browser is provided, pytest will automatically raise an error.
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]

            screenshot_path = f"screenshots/{item.name}.png"

            screenshot = page.screenshot(path=screenshot_path)

            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            print(f"Screenshot saved: {screenshot_path}")

@pytest.fixture()
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.enter_username("UFFPS1042A")
    login_page.wait_for_captcha()
    login_page.next_button()
    login_page.login_with_password()
    login_page.enter_password("password")
    login_page.click_login_button()

    yield page

def pytest_addoption(parser):      #this is hook for adding command line options to pytest. It allows you to define custom command line arguments that can be used when running tests. In this case, the code is adding a "--browser" option that allows the user to specify which browser to use for testing (default is "chromium").
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "edge"],
    )


    
      