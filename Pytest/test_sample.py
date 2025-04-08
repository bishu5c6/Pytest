import time
from selenium import webdriver
import pytest
import xdist




def test_one():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    time.sleep(5)
    driver.quit()

def test_two():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    driver.quit()

def test_three():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium143.blogspot.com/")
    time.sleep(5)
    driver.quit()


def test_four():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium-by-arun.blogspot.com/")
    time.sleep(5)
    driver.quit()

def test_five():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/")
    time.sleep(5)
    driver.quit()

def test_six():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://seleniumone-by-arun.blogspot.com/")
    time.sleep(5)
    driver.quit()

#when we exectue it will run in sequential manner
#if you run them in parallel mode use xtest