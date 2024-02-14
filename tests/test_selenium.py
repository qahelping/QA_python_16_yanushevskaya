from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_chrome(driver):
    driver.get('https://pypi.org/project/pytest/')
    cookie = {'name': 'test', 'value': 'value'}
    driver.add_cookie(cookie)
    test_cookie = driver.get_cookie('test')
    driver.delete_cookie(cookie)

    assert cookie['name'] == test_cookie['name']

def test_navigate_to_shop(driver):
    driver.get('https://markformelle.by/magaziny/')
    assert driver.title == 'Магазин Mark Formelle'


def test_navigate_to_shop_from_menu(driver):
    base_page = BasePage(driver)
    driver.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[1]/a'
    element = driver.find_element(By.XPATH, xpath)

    base_page.force_click(element)

    assert driver.title == 'Магазины Mark Formelle'
    assert driver.current_url == 'https://markformelle.by/magaziny/'


def test_get_attribute(driver):
    driver.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[1]/a'
    element = driver.find_element(By.XPATH, xpath)

    assert element.get_attribute('href') in 'https://markformelle.by/magaziny/'


def test_get_text(driver):
    driver.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[1]/a'
    element = driver.find_element(By.XPATH, xpath)

    assert element.text == 'Магазины'


def test_scroll_to(driver):
    base_page = BasePage(driver)
    driver.get('https://markformelle.by/')
    base_page.scroll_to()


def test_send_keys(driver):
    driver.get('https://www.google.com/')

    css = '[class="gLFyf"]'
    element = driver.find_element(By.CSS_SELECTOR, css)

    element.send_keys('selenium python')
    element.submit()
    assert 'selenium python' in driver.title


def test_is_displayed(driver):
    driver.get('https://www.google.com/')

    css = '[class="gLFyf"]'
    element = driver.find_element(By.CSS_SELECTOR, css)
    assert element.is_displayed()
