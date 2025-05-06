#Creating this test case to work with CSS selectors
#In this we use 4 types of comination we as we mentioned in the previous program
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#Now give the path to the drivers loction using a object called serv_obj
#serv_obj=Service("D:\Practice Daily\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#Creating a instance or other object to call the browser
#driver=webdriver.Chrome(service=serv_obj)
driver=webdriver.Chrome()
#Privide the url to the browser that to be tested
driver.get("https://www.facebook.com/")
#To maximize the window we use below function
driver.maximize_window()
#to maintain the browser for certain amout of time we need to use sleep function we need also import time module before using them
time.sleep(2)
#Using Tag and class 
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
time.sleep(2)
#Using Tag and id  
driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("abc@123")
time.sleep(2)
#Using Tag and Attribute
driver.find_element(By.CSS_SELECTOR,"button[data-testid=royal_login_button]").click()
time.sleep(2)
#Using Tag,Class and Attribute
driver.find_element(By.CSS_SELECTOR,"a._42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy[data-testid=open-registration-form-button]")
time.sleep(2)
driver.close()

