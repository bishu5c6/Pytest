

import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import allure

from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class test_mutiple_test_cases:
    def test_with_login_credentails(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("pinnikabiswanth@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(),name="test_with_login_credentails",attachment_type=AttachmentType.PNG)


    def test_without_entering_credential(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("")
        self.driver.find_element(By.ID,"input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_warning_message)



#how to run these file pytest test_multiple_test_cases.py with screenshot file in it
#Pytest tests\test_multiple_test_cases.py --alluredir="./reports"

