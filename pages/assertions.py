from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Assertions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_text(self, text, locator):
        assert "Elemental Selenium" == self.get_text(
            '//*[@id="page-footer"]/div/div/a'
        ), f"Text  not found"
