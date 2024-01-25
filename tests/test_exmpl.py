import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function', autouse=True)
def driver_firefox():
    print("Start function\n")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.minimize_window()
    yield driver
    driver.close()
    driver.quit()
    print("Finish function\n")


@pytest.fixture(scope='session', autouse=True)
def driver_chrome():
    print("Start session\n")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
    print("Finish session\n")


@pytest.fixture(autouse=True)
def driver():
    print("Start driver\n")
    yield
    print("Finish driver\n")

def test_user():
   print("test")


def test_user2():
   print("test2")


   # session function  function session