import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By


def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    #request.cls.driver = driver
    yield
    driver.quit
@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
@allure.severity(allure.severity_level.CRITICAL)
class test_severity:
    def test_with_login_credentails(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("pinnikabiswanth@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_with_login_credentails",
                      attachment_type=AttachmentType.PNG)