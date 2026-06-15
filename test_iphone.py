"""
Test Case 1 — iPhone
─────────────────────
Steps:
  1. Navigate to Amazon.com
  2. Search for "iPhone"
  3. Click the first result
  4. Add the iPhone to the cart
  5. Print the price to the console
"""

import pytest
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from utils.logger import log

TEST_NAME = "TC1 - iPhone"
SEARCH_QUERY = "iPhone"


def test_add_iphone_to_cart(browser_page):
    """
    Search for an iPhone on Amazon, add it to the cart,
    and print its price.
    """
    page = browser_page

    # ── Step 1 & 2: Navigate and search ──────────────────────────────────────
    search = SearchPage(page)
    log(TEST_NAME, f"Navigating to Amazon and searching for '{SEARCH_QUERY}'")
    search.go_to_amazon()
    search.search_for(SEARCH_QUERY)

    # ── Step 3: Click the first result ───────────────────────────────────────
    log(TEST_NAME, "Clicking first search result")
    search.click_first_result()

    # ── Step 4 & 5: Read price and add to cart ───────────────────────────────
    product = ProductPage(page)

    title = product.get_product_title()
    log(TEST_NAME, f"Product: {title[:100]}")

    price = product.get_price()
    # ✅ Required verification — print price to console
    log(TEST_NAME, f"💰 Price: {price}")
    print(f"\n{'='*60}")
    print(f"  [TC1 - iPhone] PRICE RETRIEVED: {price}")
    print(f"{'='*60}\n")

    product.add_to_cart()
    log(TEST_NAME, "✅ Test complete")

    # Assertion — price must have been found
    assert price != "Price not found", (
        "Could not retrieve the product price. "
        "Amazon's page layout may have changed."
    )
