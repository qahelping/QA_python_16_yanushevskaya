import time

from pages.base_page import BasePage


class NewsPage(BasePage):
    TITLE = '[id="main-heading"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_title_is_visible(self):
        time.sleep(1)
        assert self.get_locator_by_css(self.TITLE), 'Title not found'
