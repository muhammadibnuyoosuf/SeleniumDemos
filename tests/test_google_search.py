from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def test_login():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.saucedemo.com")

    # Enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)
    print("we are logged in feture login")

    driver.save_screenshot("failure.png")

    # Validation
    assert "inventory" in driver.current_url

    driver.quit()