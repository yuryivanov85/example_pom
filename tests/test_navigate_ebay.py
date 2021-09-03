from pages.home_page import HomePage
import pytest


@pytest.mark.smoketest
def test_navigate_ebay(browser):
    ebay_home_page = HomePage(browser)
    ebay_home_page.navigate_to_home_page()
