from selenium.webdriver.common.by import By

from helpers import force_click, scroll_to


def test_chrome(driver_chrome):
    driver_chrome.get('https://pypi.org/project/pytest/')
    cookie = {'name': 'test', 'value': 'value'}
    driver_chrome.add_cookie(cookie)
    test_cookie = driver_chrome.get_cookie('test')
    driver_chrome.delete_cookie(cookie)

    assert cookie['name'] == test_cookie['name']


def test_firefox(driver_firefox):
    driver_firefox.get('https://pypi.org/project/pytest/')


def test_navigate_to_shop(driver_chrome):
    driver_chrome.get('https://markformelle.by/magaziny/')
    assert driver_chrome.title == 'Магазин Mark Formelle'


def test_navigate_to_shop_from_menu(driver_chrome):
    driver_chrome.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[1]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)

    force_click(driver_chrome, element)

    assert driver_chrome.title == 'Магазины Mark Formelle'
    assert driver_chrome.current_url == 'https://markformelle.by/magaziny/'


def test_get_attribute(driver_chrome):
    driver_chrome.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[1]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.get_attribute('href') in 'https://markformelle.by/magaziny/'


def test_get_text(driver_chrome):
    driver_chrome.get('https://markformelle.by/')

    xpath = '/html/body/div[3]/header/div[2]/div[1]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)

    assert element.text == 'Магазины'


def test_scroll_to(driver_chrome):
    driver_chrome.get('https://markformelle.by/')
    scroll_to(driver_chrome)


def test_send_keys(driver_chrome):
    driver_chrome.get('https://www.google.com/')

    css = '[class="gLFyf"]'
    element = driver_chrome.find_element(By.CSS_SELECTOR, css)

    element.send_keys('selenium python')
    element.submit()
    assert 'selenium python' in driver_chrome.title


def test_is_displayed(driver_chrome):
    driver_chrome.get('https://www.google.com/')

    css = '[class="gLFyf"]'
    element = driver_chrome.find_element(By.CSS_SELECTOR, css)
    assert element.is_displayed()
