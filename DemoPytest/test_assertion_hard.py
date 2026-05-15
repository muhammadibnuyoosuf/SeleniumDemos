# import time
# 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# 
# 
# def test_assertion_hard():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.testmuai.com/selenium-playground/radiobutton-demo/")
# 
#     male = driver.find_element(By.XPATH,"//input[@name='gender' and @value='Male']")
#     male.click()
#     time.sleep(5)
#     age = driver.find_element(By.XPATH,"//input[@value='5 - 15']")
#     age.click()
# 
#     time.sleep(5)
#     get_values = driver.find_element("xpath","//button[contains(text(),'Get values')]")
#     get_values.click()
# 
#     gender_value = driver.find_element(By.CSS_SELECTOR,".genderbutton").text
#     age_value = driver.find_element(By.CSS_SELECTOR,".groupradiobutton").text
#     assert gender_value == "Male","Gender mismatch"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_assertion_hard():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.maximize_window()
    driver.get("https://www.testmuai.com/selenium-playground/radiobutton-demo/")

    # Male radio button
    male = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='gender'][value='Male']")
        )
    )

    driver.execute_script("arguments[0].click();", male)

    # Re-find age element fresh
    age = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@value='5 - 15']")
        )
    )

    driver.execute_script("arguments[0].click();", age)

    # Click Get Values
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Get values')]")
        )
    )

    button.click()

    # Read results
    gender_value = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".genderbutton")
        )
    ).text

    age_value = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".groupradiobutton")
        )
    ).text

    print(gender_value)
    print(age_value)

    assert gender_value == "Male"
    assert age_value == "5 - 15"

    driver.quit()

