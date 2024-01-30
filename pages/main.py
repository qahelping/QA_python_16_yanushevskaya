from helpers import get_locator_by_class


class MainPage:
    # locataors
    MAIN_NEWS = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor'

    def __init__(self, driver):
        self.driver = driver

    def click_on_main_news(self):
        element = get_locator_by_class(self.driver, self.MAIN_NEWS)
        element.click()
