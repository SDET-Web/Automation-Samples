""" Fixtures are a key feature of Pytest that allow you to set up
and share reusable test resources and configurations
we'll cover how to define fixtures at the module level and utilize them across multiple test functions.
We'll also dive into fixture scopes, such as module and function, and discuss best practices for organizing
your fixtures. Additionally, we'll demonstrate how to use fixtures to set up browser instances and page
 contexts for efficient and maintainable test automation with Playwright.
"""
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_goto_google(page):
    page.goto("https://www.google.com")
    page.wait_for_timeout(2000)
    assert page.title() == "Google"

def test_orange(page):
    page.goto("https://www.orange.com/en")
    page.wait_for_timeout(2000)
    assert page.title() == "Corporate Website of Orange"