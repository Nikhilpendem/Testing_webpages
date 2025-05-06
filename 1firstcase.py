from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-input--active").send_keys("admin123")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-button--medium").click()
time.sleep(5)
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("login Test Passed")   
else:
    print("Login Test Failed")
driver.close()    
    
