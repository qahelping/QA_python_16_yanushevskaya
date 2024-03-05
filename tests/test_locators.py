import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


@pytest.mark.first
def test_by_name(driver):
    driver.get("https://ozon.by/")
    name = "yandex-tableau-widget"
    assert driver.find_element(By.NAME, name)


@pytest.mark.second
def test_by_id(driver):
    driver.get("https://www.wildberries.by/")
    id = "route-content"
    assert driver.find_element(By.ID, id)


@pytest.mark.second
def test_by_link_text(driver):
    driver.get("https://habr.com/ru/articles/667238/")
    text = "Научпоп"
    assert driver.find_element(By.LINK_TEXT, text)


@pytest.mark.only
def test_by_partial_link_text(driver):
    driver.get("https://habr.com/ru/articles/667238/")
    text = "готовилась"
    assert driver.find_element(By.PARTIAL_LINK_TEXT, text)


@pytest.mark.skip
def test_by_tag_name(driver):
    driver.get("https://habr.com/ru/articles/667238/")
    tag = "span"
    driver.find_element(By.TAG_NAME, tag)


@pytest.mark.skip
def test_by_class_name(driver):
    driver.get("https://habr.com/ru/articles/667238/")
    class_name = "tm-adfox-banner__container"
    elements = driver.find_elements(By.CLASS_NAME, class_name)
    assert len(elements) == 4


@pytest.mark.xfail(reason="fixing this bug right now")
def test_2(self, browser):
    pass


def test_by_name_css(driver):
    driver.get("https://ozon.by/")
    css = "[name='yandex-tableau-widget']"
    assert driver.find_element(By.CSS_SELECTOR, css)


def test_by_id_css(driver):
    driver.get("https://www.wildberries.by/")
    id = "#route-content"
    assert driver.find_element(By.CSS_SELECTOR, id)


def test_by_class_name_css(driver):
    driver.get("https://ozon.by/")
    class_name = ".da9c.dac2"
    elements = driver.find_elements(By.CSS_SELECTOR, class_name)
    assert len(elements) == 4


def test_by_class_name_cssw(driver):
    driver.get("https://ozon.by/")
    base_page = BasePage(driver)
    assert base_page.get_locator_by_class("da9c dac2")


def test_by_xpath(driver):
    driver.get("https://ozon.by/")
    xpath = "//form/button/div"
    assert driver.find_element(By.XPATH, xpath)


def test_by_xpath_attr(driver):
    driver.get("https://ozon.by/")
    xpath = '//*[@class="ag15-a"]'
    assert driver.find_element(By.XPATH, xpath)


def test_by_xpath_text(driver):
    driver.get("https://ozon.by/")
    xpath = '//*[text()="Детские товары"] '
    assert driver.find_element(By.XPATH, xpath)


def test_by_xpath_text_by_contains(driver):
    driver.get("https://ozon.by/")
    xpath = '//*[contains(text(),"Детские")]'
    assert driver.find_element(By.XPATH, xpath)


def test_by_data_id(driver):
    driver.get("https://www.avito.ru/")
    base_page = BasePage(driver)
    assert driver.find_element(base_page.get_by_data_id("1838"))
