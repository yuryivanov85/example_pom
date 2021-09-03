from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    # constructor
    def __init__(self, browser):
        self.browser = browser

    URL = "https://www.ebay.com/"
    TITLE = "Electronics, Cars, Fashion, Collectibles & More | eBay"

    # Element Locators

    SEARCH_FIELD = (By.ID, "gh-ac")

    #  All Methods for your Page
    def navigate_to_home_page(self):
        self.browser.get(self.URL)

    def assert_title(self):
        assert self.browser.title == self.TITLE

    def search_item(self, item):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(item + Keys.ENTER)

