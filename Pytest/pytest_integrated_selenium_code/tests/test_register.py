import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import allure
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class test_register:
    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Biswanth")
        self.driver.find_element(By.ID,"input-lastname").send_keys("pinnika")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID,"input-telephone").send_keys(8688856560)
        self.driver.find_element(By.ID,"input-password").send_keys(12345)
        self.driver.find_element(By.ID,"input-confirm").send_keys(12345)
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_with_login_credentails",
                      attachment_type=AttachmentType.PNG)
        time.sleep(5)


    def test_creating_with_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Biswanth")
        self.driver.find_element(By.ID,"input-lastname").send_keys("pinnika")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID,"input-telephone").send_keys(8688856560)
        self.driver.find_element(By.ID,"input-password").send_keys(12345)
        self.driver.find_element(By.ID,"input-confirm").send_keys(12345)
        self.driver.find_element(By.XPATH,"//input[@value='1'][@name='newsletter']").click()
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)
        time.sleep(5)
        self.driver.quit()


    def generate_email_time_stamp(self):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = timestamp.replace('-','_').replace(' ','_' ).replace(':','_')
        return "biswanth"+timestamp+"@gmail.com"