import pytest
from selenium import webdriver
from driverfactory.initializeDriver import InitailizeDriver
from utilities import createlog,utilfunctions
import sys
import shutil
import time

from utilities.createlog import LogGen


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
        LogGen.static_logger.info(str(item.name) + ": " + "failed")
    else:
        LogGen.static_logger.info(str(item.name) + ": " + "Passed")
    driver.close()


# # To generate ZIP file, but it did not work.
# @pytest.fixture(autouse=True, scope='session')
# def suite_teardown():
#     yield
#     # time.sleep(25)
#     print(sys.path[0] + '\\Reports')
#     shutil.make_archive('Zipped file', 'zip', sys.path[0] + '\\Reports')

# def pytest_sessionfinish(session, exitstatus):
#     print('Inside ---- pytest_sessionfinish ')
#     # shutil.make_archive('Zipped file', 'zip', '.\\Reports')
#     utilfunctions.create_zip_file()


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")  # We can pass multiple parameters


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method
