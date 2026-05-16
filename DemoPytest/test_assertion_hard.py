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
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestAssertionSoft(softest.TestCase):

    def test_assertion_soft(self):
        # Launch browser
        driver = webdriver.Chrome()

        # Open website
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Maximize window
        driver.maximize_window()

        # Find username field and enter value
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

        # Find password field and enter value
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

        # Click login button
        login_btn = driver.find_element(By.ID, "submit")
        login_btn.click()

        # Wait for page load
        time.sleep(2)

        # Assertion
        expected_text = "Logged In Successfully"

        actual_text = driver.find_element(By.TAG_NAME, "h1").text

        print("Object of expected text is: {}".format(id(expected_text)))
        print("Object of actual text is: {}".format(id(actual_text)))

        #assert expected_text == actual_text,"Displayed something else"
        #assert driver.title.__contains__("Logged In Successfully"),"Title is not displayed"
        self.soft_assert(self.assertEqual,expected_text,actual_text,"test_assertion_soft failed")
        self.soft_assert(self.assertTrue,driver.title.__contains__("Logged In Successfully"),"Title is not displayed")
        self.assert_all()

        print("Test Passed")

        # Close browser
        driver.quit()

