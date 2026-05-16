from selenium import webdriver


def test_home_page_title():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/")

    assert "Practice Test Automation" in driver.title

    driver.quit()


def test_home_page_url():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/")

    assert driver.current_url == "https://practicetestautomation.com/"

    driver.quit()