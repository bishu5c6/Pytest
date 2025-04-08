from selenium import webdriver
from selenium.webdriver.common.by import By


# def test_tutorial_ninja():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://tutorialsninja.com/demo/")
#     expected_title = "Your Store ABC"
#     actual_title = driver.title
#     assert actual_title.__eq__(expected_title)
#     driver.find_element(By.NAME,"search").send_keys("HP")
#     driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
#     assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
#     driver.quit()

#above is the example of soft assertions.
#instal pip install pytest-soft-assertions

def test_tutorial_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    expected_title = "Your Store ABC"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)
    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    driver.quit()
