import allure
import pytest
import pytest_html
from allure_commons.types import AttachmentType
from selenium import webdriver
from driverfactory.initializeDriver import InitailizeDriver
from utilities import createlog, utilfunctions
import sys
import shutil
import time
from allure_pytest import *
from allure_commons import *
import traceback

from utilities.createlog import LogGen


@pytest.fixture(autouse=True, scope='session')
def setlogs():
    createlog.LogGen.loggen()


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    extra = getattr(rep, 'extra', [])
    if rep.when == 'call' or rep.when == "setup":
        xfail = hasattr(rep, 'wasxfail')
        if (rep.skipped and xfail) or (rep.failed and not xfail):
            file_name = rep.nodeid.replace("::", "_") + ".png"
            # file_name = 'ss.png'#"screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            driver.get_screenshot_as_file(file_name)
            # if file_name:
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.image(file_name))
            # extra.append(pytest_html.extras.html(html))
        rep.extra = extra
    # return rep


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # now = datetime.now()
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
#             # _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

@pytest.fixture(autouse=True)
def setup(browser, request):
    global driver
    LogGen.static_logger.info("---------" + str(request.node.name) + ": " + "Started--------------------------------")
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
    # InitailizeDriver.init_driver(driver)
    request.cls.driver = driver


@pytest.fixture(autouse=True)
def tear_down(request):
    yield
    item = request.node
    if item.rep_call.failed:
        print(sys.path[0] + "\\Screenshots\\" + str(item.name) + '.png')
        driver.save_screenshot(sys.path[0] + "\\Screenshots\\" + str(item.name) + '.png')
        allure.attach(driver.get_screenshot_as_png(), name=str(item.name), attachment_type=AttachmentType.PNG)
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

@pytest.hookimpl(tryfirst=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    utilfunctions.create_zip_file()


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")  # We can pass multiple parameters


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method


def pytest_exception_interact(node, call, report):
    if report.failed:
        test_name = node.name
        LogGen.static_logger.error(f"---------------------*********Test '{test_name}' failed:--************----")
        traceback_str = str(call.excinfo.getrepr())
        LogGen.static_logger.error(traceback_str)
        LogGen.static_logger.info("---------*******************---------------------***********---------------")
