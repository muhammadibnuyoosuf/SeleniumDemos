from selenium import webdriver
from selenium.webdriver.common.by import By


def test_blog_navigation():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/")

    blog_link = driver.find_element(
        By.XPATH,
        "//a[contains(@href,'blog')]"
    )

    blog_link.click()

    assert "blog" in driver.current_url

    driver.quit()


def test_blog_page_title():

    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/blog/")

    assert "Blog" in driver.title

    driver.quit()