import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

def test_flipkart_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()