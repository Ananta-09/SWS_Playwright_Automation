import allure
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
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

    
      