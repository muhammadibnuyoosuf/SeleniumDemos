from selenium import webdriver
from selenium.webdriver.common.by import By


def test_logout_button_visible():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")

    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()

    logout_button = driver.find_element(By.LINK_TEXT, "Log out")

    assert logout_button.is_displayed()

    driver.quit()


def test_logout_success():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")

    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()

    driver.find_element(By.LINK_TEXT, "Log out").click()

    assert "practice-test-login" in driver.current_url

    driver.quit()