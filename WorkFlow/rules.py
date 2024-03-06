# test file should start with test_
# test name should start with test_
# ------------------------------------------------
# to see the output
# pytest -rA
# py.test
# -----------------------------------------------------
# Assertion

# def test_sam_5():
#     a = 10
#     b = 20
#     #assert b >= a,  "a is not equal to b"   # this will print the message
#     assert a.__eq__(b)

# -----------------------------------------------------
# Flags

# python --help or -h
# -v for verbose
# -rA will give the print statement

# -k  -- to run the test method by mentioning a string in the test method
# test_sample_one()      -- pytest -k one
# to run a test case with or keyword -- pytest - k "one or two"
# not to run a particular test case -- pytest -k "not one"

# -----------------------------------------------------
# Generating JUnit XML Report
# pytest -rA --junit-xml="Report1.xml"
# pytest -rA --junit-xml="Reports/rep1.xml"

# -----------------------------------------------------
# Generating HTML Report
# First install pytest-html in PyCharm IDE  --- pip install pytest-html
# Then from the settings in PYCharm find pytest-html and install it
# To generate the report pytest --html="path/report.html"

# -----------------------------------------------------
# Markers
# write the line before the test method  @pytest.mark.smoke
# run the test cases with the markers --- pytest -rA -m smoke  // This will run the smoke test cases
# or keyword --   pytest -rA -m "smoke or regression"

# -----------------------------------------------------
# Custom Markers   -- To overcome unnecessary warnings
# create a pytest.ini file under the project
# under this file, write the lines:
#
# [pytest]
# markers=smoke: this is a smoke test marker
#         regression: this is a regression test marker

# -----------------------------------------------------
# Skip a test
# pytest.mark.skip

# -----------------------------------------------------
# Expected Fail and Expected Pass
# @pytest.mark.xfail  -- if the test case fail, it will not come under the fail category instead
# , it will come under Expected fail category
# if the test case passes, it will come under Expected pass category

# -----------------------------------------------------
# Parameterization
# pytest.mark.parametrize
# Example:

# @pytest.mark.parametrize("username, password", [("arun", "1234"), ("varun", "4569"), ("tarun", "98455")])
# def test_sam_7(username, password):
#     print(username + "___" + password)

# -----------------------------------------------------
# Executing pytest from command line
# go to the root location and open cmd

# -----------------------------------------------------
# Group the test
# pytest -vs -m "smoke"

# -----------------------------------------------------
# Fixtures  -- before and after method
# run some setup code -- Launching browser, opening url,
# closure -- logout

# Example:

# @pytest.fixture()
# def setup_and_teardown():
#     print("##Launch Browser")
#     print("#### Open App")
#     yield
#     print("### Logout from app")
#     print("### Close browser")

# -----------------------------------------------------
# Creating a fixture inside conftest.py file under the package
# We still need to give the name of the fixture in every test case method

# -----------------------------------------------------
# Using autouse attribute in PyTest fixture  -- no need to mention the fixture name in every test name
# @pytest.fixture(autouse=True)

# -----------------------------------------------------
# Using scope attribute in PyTest fixture
# @pytest.fixture(scope="function")  -- scope can be function, session, class, package, module
# if "function" -- the fixture will run before and after every test method   # by default, the scope is set as function
# if "session" -- the fixture will run before all the tests  once and after all the test once

# -----------------------------------------------------
# Parallel Execution of Tests using pytest-xdist
# Install pytest-xdist  ---   pip install pytest-xdist
# pytest -n 5     ---- 5 represents the number of worker group

# -----------------------------------------------------
# Hook functions which act like fixtures in PyTest
# setup_function(function), teardown_function(function), setup_module(module) and teardown_module(module)
# module will run once before all the test cases run and after all the test cases run
# Example:

# def setup_function(function):
#     print("##### hook Launch browse")
#
#
# def teardown_function(function):
#     print("##### hook Close browser")

# -----------------------------------------------------
# Soft Assertions
# Install the package  -->  pip install pytest-soft-assertions
# Usage  --> through command line  -->  pytest --soft-asserts

# ----------------------------------------------------------------------
#  Use the same conftest.py file for all test class using decorator
#  1. All the test cases should be under a class
#  2. above the Class Name use a fixture annotaion such as
#  @pytest.mark.usefixtures("setup_and_teardown")
#  class Testsearch:
#       def test_t1(self):
#       def test_t2(self):


# use request fixture in the setup_and_teardown
# @pytest.fixture()
# def setup_and_teardown(request):
#       driver = webdriver.Chrome()
#       driver.maximize.window()
#       driver.get('url')
#       request.cls.driver = driver
#       yield:
#       driver.quit()

#  now use self.driver in every test class methods


# ----------------------------------------------------------------------
#  Generating Allure Reports
#  1. Install Java, Node.js, Allure command-line tool
#  In cmd --> npm install -g allure-commandline
#  allure --version
#  Users > ..> AppData > Roaming > npm > node-modules > allure-commandline > bin  ----> add it to env variables
#  Users > ..> AppData > Roaming > npm   ----> even this
#  pip install allure-pytest
#  to generate allure reports along with test case execution  --->  pytest --alluredir="./reports"
#  Run in command line under the project folder --> allure serve "./reports"

# ----------------------------------------------------------------------
#  Attaching screenshots in Allure Reports
#  Inside the test case method add this line at any line where you want the ss to be cptured
#  allure.attach(self.driver.get_screenshot_as_png(), name="anyname", attachment_type=AttachmentType.PNG)

# ----------------------------------------------------------------------
#  Adding severity levels with the help of Decorators in Allure Report
#  At class level, at test level ---> @allure.severity(allure.severity_level.MINOR)  --> MINOR, NORMAL, TRIVIAL, CRITICAL
#  We can write it on the top of test_method:  --> test level
#   @allure.severity(allure.severity_level.MINOR)
#   def test_search_func(self):
#  We can write it on the top of class:  --> class level
#  @allure.severity(allure.severity_level.MINOR)
#  class SearchTest:

# ----------------------------------------------------------------------
#  Sharing the Allure Reports
#  stored at a temporary location
#  using an external website to generate the link for accessing the report

# ----------------------------------------------------------------------
#  Taking screenshots only on Failure  --> refer this link: github.com/pytest-dev/issues/230
#  add this line of code in the conftest.py

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep


# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#           allure.attach(.driver.get_screenshot_as_png(), name="anyname", attachment_type=AttachmentType.PNG)
#

#  Now go to every test class and at the top of it, mention this fixture
#  @pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
#  class TestClass:
#

# ----------------------------------------------------------------------
#  Parameterize fixtures using params
#  parameterize the setup_and_teardown fixture in conftest.py file
# Every test will run for three browser


# @pytest.fixture(params=["chrome", "firefox", "edge"])
# def setup_and_teardown(request):
#     global driver
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     elif request.param == "edge":
#         driver = webdriver.Edge()
#     driver.maximize.window()
#     driver.get('url')
#     request.cls.driver = driver
#     yield
#     driver.quit()

# ----------------------------------------------------------------------
#  Passing options from pytest commands
#  In conftest.py file, create this method:

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--platform")

#  now make changes to setup_and_teardown fixture
# @pytest.fixture()
# def setup_and_teardown(request):
#     global driver
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     driver.maximize.window()
#     driver.get('url')
#     request.cls.driver = driver
#     yield
#     driver.quit()

#  go to the terminal and write it down:
#  pytest --browser chrome

