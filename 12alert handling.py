from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import time
serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://mypage.rediff.com/")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window
# driver.find_element(By.XPATH,"//input[@value=' Go ']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.send_keys("Welcome")
time.sleep(2)
# alert.accept()
alert.dismiss()
