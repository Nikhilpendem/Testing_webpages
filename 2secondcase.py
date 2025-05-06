from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.find_element(By.NAME,"user-name").send_keys("visual_user")
time.sleep(5)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.ID,"login-button").click()
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("login Test Passed")   
else:
    print("Login Test Failed")
driver.close()  