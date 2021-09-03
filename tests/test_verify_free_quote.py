import pytest

@pytest.mark.regressiontest
def test_verify_free_quote(browser):
    browser.get("www.freequote.com")