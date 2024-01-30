from selenium.webdriver.common.by import By


def get_by_class_css(selector):
    return f'[class="{selector}"]'


def get_locator_by_class(driver, selector):
    selector = get_by_class_css(selector)
    return driver.find_element(By.CSS_SELECTOR, selector)


def get_locator_by_css(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


def get_by_data_id(data_id):
    return f"//*[data-id={data_id}]"
