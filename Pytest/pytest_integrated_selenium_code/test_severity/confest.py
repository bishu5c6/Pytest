import allure
import driver
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--platform")

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",attachment_type=AttachmentType.PNG)
        


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" +rep.when, rep)
    return rep


# @pytest.fixture(scope='class')
@pytest.fixture(params=["chrome","firefox","edge"])
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    if request.param =="chrome":
        driver = webdriver.Chrome()
    elif request.param=="firefox":
        driver = webdriver.Firefox()
    elif request.param =="edge":
        driver = webdriver.Edge()
    else:
        print("no browser found")
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    request.cls.driver = driver
    yield
    driver.quit

#passing options from pytest commands.
#hoe to run pytest tests\test_search.py --browser chrome
@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        print("No browser found")

    driver.maximize_window()
    driver.get()
    request.cls.driver = driver
    yield
    driver.quit
