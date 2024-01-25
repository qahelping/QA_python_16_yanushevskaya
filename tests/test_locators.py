import pytest
from selenium.webdriver.common.by import By

from locators import get_by_data_id, get_locator_by_class

@pytest.mark.first
def test_by_name(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    name = 'yandex-tableau-widget'
    assert driver_chrome.find_element(By.NAME, name)

# @pytest.mark.second
# def test_by_id(driver_chrome):
#     driver_chrome.get('https://www.wildberries.by/')
#     id = 'route-content'
#     assert driver_chrome.find_element(By.ID, id)
#
# @pytest.mark.second
# def test_by_link_text(driver_chrome):
#     driver_chrome.get('https://habr.com/ru/articles/667238/')
#     text = 'Научпоп'
#     assert driver_chrome.find_element(By.LINK_TEXT, text)

@pytest.mark.only
def test_by_partial_link_text(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    text = 'готовилась'
    assert driver_chrome.find_element(By.PARTIAL_LINK_TEXT, text)

@pytest.mark.skip
def test_by_tag_name(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    tag = 'span'
    driver_chrome.find_element(By.TAG_NAME, tag)

@pytest.mark.skip
def test_by_class_name(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    class_name = 'tm-adfox-banner__container'
    elements = driver_chrome.find_elements(By.CLASS_NAME, class_name)
    assert len(elements) == 4


@pytest.mark.xfail(reason="fixing this bug right now")
def test_2(self, browser):
   pass


#
# def test_by_name_css(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     css = "[name='yandex-tableau-widget']"
#     assert driver_chrome.find_element(By.CSS_SELECTOR, css)
#
#
# def test_by_id_css(driver_chrome):
#     driver_chrome.get('https://www.wildberries.by/')
#     id = '#route-content'
#     assert driver_chrome.find_element(By.CSS_SELECTOR, id)
#
#
# def test_by_class_name_css(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     class_name = '.da9c.dac2'
#     elements = driver_chrome.find_elements(By.CSS_SELECTOR, class_name)
#     assert len(elements) == 4
#
#
# def test_by_class_name_cssw(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     assert get_locator_by_class(driver_chrome, 'da9c dac2')
#
#
# def test_by_xpath(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     xpath = '//form/button/div'
#     assert driver_chrome.find_element(By.XPATH, xpath)
#
#
# def test_by_xpath_attr(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     xpath = '//*[@class="ag15-a"]'
#     assert driver_chrome.find_element(By.XPATH, xpath)
#
#
# def test_by_xpath_text(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     xpath = '//*[text()="Детские товары"] '
#     assert driver_chrome.find_element(By.XPATH, xpath)
#
#
# def test_by_xpath_text_by_contains(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     xpath = '//*[contains(text(),"Детские")]'
#     assert driver_chrome.find_element(By.XPATH, xpath)
#
#
# def test_by_data_id(driver_chrome):
#     driver_chrome.get('https://www.avito.ru/')
#     assert driver_chrome.find_element(get_by_data_id('1838'))
