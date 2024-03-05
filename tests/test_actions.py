import time
import pytest
from selenium.webdriver.common.by import By

from data import DROPDOWN_URL
from data.ulrs import INPUTS
from pages.assertions import Assertions
from pages.base_page import BasePage


@pytest.mark.first
def test_by_get(driver):
    driver.get(DROPDOWN_URL)

    locator = '//*[@id="dropdown"]/option[2]'

    base_page = BasePage(driver)
    assert 'selected' == base_page.get_attribute(locator, 'selected')


@pytest.mark.first
def test_send(driver):
    driver.get(INPUTS)

    locator = '//*[@id="content"]/div/div/div/input'

    base_page = BasePage(driver)
    base_page.fill(locator, '111')

@pytest.mark.first
def test_select(driver):
    driver.get(DROPDOWN_URL)

    locator = '//*[@id="dropdown"]'

    base_page = BasePage(driver)
    base_page.select_by_value(locator, '1')

    time.sleep(5)


@pytest.mark.first
def test_select(driver):
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    base_page = BasePage(driver)
    base_page.click_on('//*[@id="content"]/div/ul/li[1]/button')
    base_page.close_alert()

    time.sleep(5)


@pytest.mark.first
def test_select2(driver):
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    base_page = BasePage(driver)
    handle1 = driver.current_window_handle
    base_page.click_on('//*[@id="page-footer"]/div/div/a')
    time.sleep(5)
    handle2 = driver.current_window_handle
    assert handle1 == handle2
    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    handle3 = driver.current_window_handle
    driver.close()
    assert handle1 == handle2 == handle3

    time.sleep(5)


@pytest.mark.first
def test_iframe(driver):
    driver.get('https://the-internet.herokuapp.com/iframe')
    base_page = BasePage(driver)

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '[id="mce_0_ifr"]'))
    assert 'Your content goes here.' == base_page.get_text('//p')
    driver.switch_to.default_content()
    Assertions(driver).asssert_text('Elemental Selenium', '//*[@id="page-footer"]/div/div/a')


@pytest.mark.first
def test_send_file(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    base_page = BasePage(driver)

    base_page.fill('//*[@id="file-upload"]',
                   '/Users/elenayanushevskaya/Documents/84A70C57-4FB6-4744-8476-063957F9AC2C.png')
    assert True


@pytest.mark.first
def test_cookie(driver):
    driver.get('https://the-internet.herokuapp.com/abtest')
    base_page = BasePage(driver)

    cookie = {'name': 'optimizelyOptOut', 'value': 'true'}
    driver.add_cookie(cookie)
    text1 = base_page.get_text('//*[@id="content"]/div/h3')
    driver.refresh()
    text2 = base_page.get_text('//*[@id="content"]/div/h3')
    assert text1 != text2
    assert text1 == text2


def test_cookie2(driver):
    driver.get("https://the-internet.herokuapp.com/abtest")

    assert True
