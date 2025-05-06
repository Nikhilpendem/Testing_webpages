#  pip install pytest pytest-html
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="class")
def setup(request):
    # Set up the ChromeDriver and start the browser
    serv_obj = Service("path/to/your/chromedriver")
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestSauceDemo:
    
    def test_login(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        assert "Swag Labs" in self.driver.title

    def test_add_to_cart(self):
        self.driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button").click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']").is_displayed()

    def test_checkout(self):
        self.driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']").click()
        self.driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]").click()
        time.sleep(2)
        assert self.driver.find_element(By.LINK_TEXT, "CANCEL").is_displayed()
