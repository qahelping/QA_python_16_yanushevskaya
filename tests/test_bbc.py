from pages import (MainPage, NewsPage)

import pytest



@pytest.mark.bbc
def test_open_main_new(driver):
    main_page = MainPage(driver)
    main_page.goto()


@pytest.mark.bbc
def test_open_main_new(driver):
    main_page = MainPage(driver)
    main_page.goto()



