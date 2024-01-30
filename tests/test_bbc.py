from pages.main import MainPage
from pages.news import NewsPage

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver


@pytest.fixture(scope='session', autouse=False)
def driver_chrome():
    print("Start driver_chrome\n")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.bbc.com/news')
    yield driver
    driver.close()
    driver.quit()
    print("Finish driver_chrome\n")


@pytest.mark.bbc
def test_open_main_new(driver_chrome):
    main_page = MainPage(driver_chrome)
    main_page.click_on_main_news()

    news_page = NewsPage(driver_chrome)
    news_page.assert_that_title_is_visible()
