import pytest

from data import DROPDOWN_URL
from pages.base_page import BasePage


@pytest.mark.first
def test_wait_for_element(driver):
    driver.get(DROPDOWN_URL)

    locator = '//*[@id="dropdown"]/option[2]'

    base_page = BasePage(driver)
    assert base_page.wait_for(locator)
