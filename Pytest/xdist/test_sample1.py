from selenium import webdriver
import time

def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    time.sleep(5)
    driver.quit()








