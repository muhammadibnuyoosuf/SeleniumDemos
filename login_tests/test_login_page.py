from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")

    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()

    assert "logged-in-successfully" in driver.current_url

    driver.quit()


def test_invalid_username():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("incorrectUser")

    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()

    error = driver.find_element(By.ID, "error").text

    assert error == "Your username is invalid!"

    driver.quit()


def test_invalid_password():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")

    driver.find_element(By.ID, "password").send_keys("wrongPassword")

    driver.find_element(By.ID, "submit").click()

    error = driver.find_element(By.ID, "error").text

    assert error == "Your password is invalid!"

    driver.quit()


def test_empty_username():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()

    assert "practice-test-login" in driver.current_url

    driver.quit()


def test_empty_password():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")

    driver.find_element(By.ID, "submit").click()

    assert "practice-test-login" in driver.current_url

    driver.quit()