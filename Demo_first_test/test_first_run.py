from selenium import webdriver

def test_lambda_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.testmuai.com/selenium-playground/")
    print(f'urls {driver.current_url}')



def test2_lambda_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print(f'urls {driver.title}')