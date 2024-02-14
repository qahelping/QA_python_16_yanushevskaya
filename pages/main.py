from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MainLocators()

    def click_on_main_news(self):
        self.click_on(self.locators.MAIN_NEWS)

    def goto(self):
        self.driver.get('https://www.bbc.com/news')

    def assert_text(self, text, locator):
        assert 'Elemental Selenium' == base_page.get_text('//*[@id="page-footer"]/div/div/a')
