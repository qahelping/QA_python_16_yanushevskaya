import time

from helpers import get_locator_by_css


class NewsPage:
    TITLE = '[id="main-heading"]'

    def __init__(self, driver):
        self.driver = driver

    def assert_that_title_is_visible(self):
        time.sleep(1)
        assert get_locator_by_css(self.driver, self.TITLE), 'Title not found'
