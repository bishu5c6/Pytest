# from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()


def test_search_for_a_valid_product(setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    time.sleep(5)



def test_search_for_invalid_valid_product(setup_and_teardown):
    driver.find_element(By.NAME,"search").send_keys("Honda")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    expected_text ="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    time.sleep(5)


def test_search_for_product_without_entering_anything(setup_and_teardown):
    # driver.find_element(By.NAME,"search").send_keys("Honda")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    expected_text ="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    time.sleep(5)
