import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from data import DROPDOWN_URL
from data.ulrs import CONTEXT_URL, INPUTS
from pages.base_page import BasePage


@pytest.mark.first
def test_wait_for_element(driver):
    driver.get(DROPDOWN_URL)

    locator = '//*[@id="dropdown"]/option[2]'

    base_page = BasePage(driver)
    assert base_page.wait_for(locator)
