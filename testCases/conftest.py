import pytest
from selenium import webdriver
from driverfactory.initializeDriver import InitailizeDriver
from utilities import createlog
import sys


@pytest.fixture(autouse=True, scope='session')
def setlogs():
    createlog.LogGen.loggen()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True)
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    InitailizeDriver.init_driver(driver)


@pytest.fixture(autouse=True)
def tear_down(request):
    yield
    item = request.node
    if item.rep_call.failed:
        print(sys.path[0] + "\\Screenshots\\" + str(item.name) + '.png')
        driver.save_screenshot(sys.path[0] + "\\Screenshots\\" + str(item.name) + '.png')
    driver.close()


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method
