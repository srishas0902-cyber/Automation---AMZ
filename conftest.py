"""
conftest.py — pytest fixtures shared across all tests.

Parallel execution is enabled via pytest-xdist (-n flag).
Each worker gets its own Playwright instance and browser context,
so tests are fully isolated.
"""

import pytest
from playwright.sync_api import sync_playwright
from utils.browser_factory import BrowserFactory


@pytest.fixture(scope="function")
def browser_page(request):
    """
    Fixture that yields a ready-to-use Playwright page.
    Automatically closes the browser after the test finishes.

    The test name is passed to LambdaTest so each run is labelled
    correctly in the cloud dashboard.
    """
    test_name = request.node.name

    with sync_playwright() as playwright:
        browser, page = BrowserFactory.create_browser(playwright, test_name=test_name)
        yield page
        browser.close()
