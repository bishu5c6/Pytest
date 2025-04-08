import time

from selenium import webdriver





def test_one():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    driver.maximize_window()
    time.sleep(5)

def test_two():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=05TFL3QZ34A")
    driver.maximize_window()
    time.sleep(5)


def test_three():
    driver = webdriver.Chrome()
    driver.get("https://learning.postman.com/")
    driver.maximize_window()
    time.sleep(5)




