from pages.home_page import HomePage
import pytest


@pytest.mark.smoketest
def test_verify_ebay_title(browser):
    ebay_home_page = HomePage(browser)
    ebay_home_page.navigate_to_home_page()
    ebay_home_page.assert_title()
    ebay_home_page.search_item("macbook pro")


