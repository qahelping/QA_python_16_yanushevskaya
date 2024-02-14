from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def force_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def click_on(self, locator):
        print(f'click on {locator}')
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def get_by_class_css(self, selector):
        return f'[class="{selector}"]'

    def get_locator_by_class(self, selector):
        selector = self.get_by_class_css(selector)
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def get_locator_by_css(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def get_by_data_id(self, data_id):
        return f"//*[data-id={data_id}]"

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(By.XPATH, locator)
        return element.get_attribute(attribute)

    def get_text(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element.text

    def fill(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(text)

    def clear_input(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()

    def select_by_value(self, locator, value):
        select = Select(self.driver.find_element(By.XPATH, locator))
        select.select_by_value(value)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def close_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.close()

    def wait_for(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not find"

    def wait_and_click(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element.click()
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not clickable"

    def wait_while_disappear(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until_not(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not clickable"
