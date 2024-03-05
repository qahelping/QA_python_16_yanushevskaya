from datetime import datetime

import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def driver_firefox(headless):
    options = webdriver.FirefoxOptions()
    if headless == "yes":
        options.add_argument("--headless")
    return webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=options
    )


def driver_chrome(headless):
    chrome_options = webdriver.ChromeOptions()
    if headless == "yes":
        chrome_options.add_argument("--headless")

    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )


@pytest.fixture(scope="session", autouse=False)
def driver(request):
    print("Start driver\n")

    headless = request.config.getoption("--headless")
    browser = request.config.getoption("--browser")
    driver = None

    if browser == "chrome":
        driver = driver_chrome(headless)
    if browser == "firefox":
        driver = driver_firefox(headless)

    driver.minimize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()
    print("Finish driver_firefox\n")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     yield
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             driver = request.node.funcargs['selenium_driver']
#             take_screenshot(driver, request.node.nodeid)
#             print("executing test failed", request.node.nodeid)


def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace(
        "/", "_"
    ).replace("::", "__")
    driver.save_screenshot(file_name)


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="yes",
        help="Run browser in headless mode",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type of browser",
    )
