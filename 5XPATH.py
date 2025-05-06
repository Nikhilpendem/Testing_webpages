#Using XPATH Nothing but the XML path
#Works on Document Object Model(DOM) 
#In this we use two methods to get the value of the element
#1.Absolute and 2.Relative XPATH
#Absolute XPATH works always from root note and use only tags/nodes i.e \html\....
#Relative XPATH directly jumps to the mentioned attribute and works we use only attributes here i.e .//c[attribute_name]/...
#Go from bottm to top will be the best approach
#In this we use OR,AND,CONTAINS(),STARTS-WITH() and TEXT()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time
#Iam not using any location because i choose default scripts
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)
#Absolute XPATH
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
time.sleep(2)
#Relative XPATH
driver.find_element(By.XPATH," //input[@placeholder='Password']").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(2)
#CONTAINS()
driver.find_element(By.XPATH,"//a[contains(@href,'/web/index.php/leave/viewLeaveModule')]").click()
time.sleep(2)
#STARTS-WITH()
driver.find_element(By.XPATH,"//input[starts-with(@placeholder,'Type for hints...')]").send_keys("ABC@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Dashboard']").click()
driver.close()
